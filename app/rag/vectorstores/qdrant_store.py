from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    SparseVectorParams,
    VectorParams,
)

from langchain_qdrant import (
    FastEmbedSparse,
    QdrantVectorStore,
    RetrievalMode,
)

from app.config import settings
from app.rag.embeddings.embedding_service import EmbeddingService


class QdrantStore:

    def __init__(self):

        self.client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY,
        )

        self.collection_name = settings.QDRANT_COLLECTION_NAME

        self.embeddings = (
            EmbeddingService()
            .get_embeddings()
        )

        self.sparse_embeddings = FastEmbedSparse(
            model_name=settings.SPARSE_MODEL,
        )

        self._create_collection()

        self.vector_store = QdrantVectorStore(
            client=self.client,
            collection_name=self.collection_name,
            embedding=self.embeddings,
            sparse_embedding=self.sparse_embeddings,
            retrieval_mode=RetrievalMode.HYBRID,
        )

    def _create_collection(self):

        collections = self.client.get_collections()

        existing = [
            collection.name
            for collection in collections.collections
        ]

        if self.collection_name in existing:
            return

        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE,
            ),
            sparse_vectors_config={
                "langchain-sparse": SparseVectorParams()
            },
        )

    def add_documents(
        self,
        documents,
    ):

        self.vector_store.add_documents(
            documents=documents,
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

    def as_retriever(
        self,
        **kwargs,
    ):

        return self.vector_store.as_retriever(
            **kwargs,
        )