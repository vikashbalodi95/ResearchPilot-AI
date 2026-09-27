from app.services.pdf_service import PDFService
from app.services.text_chunker import TextChunker


class DocumentService:

    def __init__(self):
        self.pdf_service = PDFService()
        self.text_chunker = TextChunker()

    def process_pdf(self, file_path: str) -> list[str]:
        text = self.pdf_service.extract_text(file_path)

        if not text.strip():
            return []

        chunks = self.text_chunker.split_text(text)

        return chunks