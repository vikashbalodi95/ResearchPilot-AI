import asyncio

from app.services.embedding_service import EmbeddingService
from app.services.vector_store_service import VectorStoreService
from app.services.groq_service import GroqService


async def main():

    embedding_service = EmbeddingService()
    vector_store = VectorStoreService()
    groq_service = GroqService()

    question = "What model was used for medical image classification?"

    # 1. Question → Embedding
    question_embedding = embedding_service.generate_embeddings(
        [question]
    )[0]

    # 2. Embedding → Relevant Chunks
    results = vector_store.search(
        query_embedding=question_embedding,
        top_k=3
    )

    # 3. Extract chunks
    documents = results["documents"][0]

    # 4. Chunks → Context
    context = "\n\n".join(documents)

    print("\nRetrieved Context:\n")
    print(context)

    # 5. Context + Question → Groq
    answer = await groq_service.generate_response(
        prompt=question,
        context=context
    )

    print("\nAnswer:\n")
    print(answer)


if __name__ == "__main__":
    asyncio.run(main())