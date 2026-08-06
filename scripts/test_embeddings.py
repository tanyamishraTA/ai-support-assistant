from app.rag.embeddings.embedding_service import EmbeddingService

embedding_service = EmbeddingService()

embeddings = embedding_service.get_embeddings()

vector = embeddings.embed_query(
    "What is the leave policy?"
)

print(f"Vector Dimension: {len(vector)}")

print(vector[:10])