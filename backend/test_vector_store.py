from app.services.embedding_service import EmbeddingService
from app.services.vector_store_service import VectorStoreService


chunks = [
    "Artificial intelligence is transforming healthcare.",
    "The researchers used a convolutional neural network for medical image classification.",
    "The experiment achieved 94 percent accuracy."
]

embedding_service = EmbeddingService()
vector_store = VectorStoreService()

embeddings = embedding_service.generate_embeddings(chunks)

vector_store.add_documents(
    chunks,
    embeddings
)

print("Chunks:", len(chunks))
print("Embeddings:", len(embeddings))
print("Vector dimension:", len(embeddings[0]))
print("Documents stored successfully!")