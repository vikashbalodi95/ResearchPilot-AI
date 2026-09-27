from app.services.embedding_service import EmbeddingService
from app.services.vector_store_service import VectorStoreService


class RetrievalTool:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStoreService()

    def retrieve(self, query: str, top_k: int = 3):

        query_embedding = (
            self.embedding_service.generate_embeddings(
                [query]
            )[0]
        )

        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        documents = results["documents"][0]

        return documents