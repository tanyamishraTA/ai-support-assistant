from langchain_qdrant import (
    FastEmbedSparse,
    QdrantVectorStore,
    RetrievalMode,
)

from app.config import settings
from app.rag.embeddings.embedding_service import EmbeddingService


class QdrantStore:

    def __init__(self):

        self.embeddings = EmbeddingService().get_embeddings()

        self.sparse_embeddings = FastEmbedSparse(
            model_name=settings.SPARSE_MODEL,
        )

        self.vector_store = QdrantVectorStore.from_documents(
            documents=[],
            embedding=self.embeddings,
            sparse_embedding=self.sparse_embeddings,
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY,
            collection_name=settings.QDRANT_COLLECTION_NAME,
            retrieval_mode=RetrievalMode.HYBRID,
            force_recreate=True,
        )

    def add_documents(self, documents):

        self.vector_store.add_documents(
            documents=documents
        )

    def similarity_search(
        self,
        query: str,
        k: int = 10,
    ):

        return self.vector_store.similarity_search(
            query=query,
            k=k,
        )

    def as_retriever(self, **kwargs):

        return self.vector_store.as_retriever(
            **kwargs
        )