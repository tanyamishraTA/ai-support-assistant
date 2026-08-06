from langchain_core.documents import Document

from app.rag.vectorstores.qdrant_store import QdrantStore


class HybridRetriever:

    def __init__(self):

        self.vector_store = QdrantStore()

    def retrieve(
        self,
        query: str,
        k: int = 10,
    ) -> list[Document]:

        return self.vector_store.similarity_search(
            query=query,
            k=k,
        )