from langchain_core.documents import Document

from app.rag.vectorstores.qdrant_store import QdrantStore


class RetrievalService:

    def __init__(self):

        self.vector_store = QdrantStore()

    def retrieve(
        self,
        question: str,
        k: int = 10,
    ) -> list[Document]:

        return self.vector_store.similarity_search(
            query=question,
            k=k,
        )