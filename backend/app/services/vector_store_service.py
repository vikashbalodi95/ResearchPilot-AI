from pathlib import Path

import chromadb


class VectorStoreService:

    def __init__(self):
        database_path = Path(__file__).resolve().parents[3] / "chroma_db"
        self.client = chromadb.PersistentClient(
            path=str(database_path)
        )

        self.collection = self.client.get_or_create_collection(
            name="research_documents"
        )

    def add_documents(
        self,
        chunks: list[str],
        embeddings: list[list[float]],
        document_id: str = "document"
    ):
        ids = [
            f"{document_id}_chunk_{index}"
            for index in range(len(chunks))
        ]

        self.collection.upsert(
            ids=ids,
            documents=chunks,
            embeddings=embeddings
        )

    def search(
        self,
        query_embedding: list[float],
        top_k: int = 3
    ):
        if self.collection.count() == 0:
            return {"documents": [[]]}

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results           