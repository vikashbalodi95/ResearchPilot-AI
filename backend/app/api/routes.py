import os
import shutil
import tempfile

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File

from app.models.chat import ChatRequest, ChatResponse
from app.services.document_service import DocumentService
from app.services.embedding_service import EmbeddingService
from app.services.groq_service import GroqService
from app.services.vector_store_service import VectorStoreService
from app.utils.validators import is_valid_question, sanitize_filename


router = APIRouter()


def get_groq_service():
    return GroqService()


@router.get("/")
def root():
    return {
        "message": "Welcome to ResearchPilot AI 🚀"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    groq_service: GroqService = Depends(get_groq_service),
):

    if not is_valid_question(request.prompt):
        raise HTTPException(
            status_code=400,
            detail="Prompt must be between 5 and 1000 characters."
        )

    embedding_service = EmbeddingService()
    vector_store = VectorStoreService()
    question_embedding = embedding_service.generate_embeddings([request.prompt])[0]
    search_results = vector_store.search(question_embedding, top_k=3)
    documents = search_results.get("documents", [[]])[0]
    context = "\n\n".join(documents)

    ai_response = await groq_service.generate_response(request.prompt, context=context)

    return ChatResponse(
        response=ai_response
    )


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    safe_name = sanitize_filename(file.filename or "document.pdf")
    document_id = os.path.splitext(safe_name)[0][:60] or "document"

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temporary_file:
        shutil.copyfileobj(file.file, temporary_file)
        temporary_path = temporary_file.name

    try:
        document_service = DocumentService()
        chunks = document_service.process_pdf(temporary_path)

        if not chunks:
            raise HTTPException(status_code=400, detail="Could not extract readable text from this PDF.")

        embedding_service = EmbeddingService()
        vector_store = VectorStoreService()
        embeddings = embedding_service.generate_embeddings(chunks)
        vector_store.add_documents(chunks, embeddings, document_id=document_id)
    finally:
        os.unlink(temporary_path)

    return {
        "message": "PDF processed successfully",
        "filename": file.filename,
        "chunks": len(chunks)
    }