from langchain_core.documents import Document

from app.rag.reranker.cross_encoder_reranker import (
    CrossEncoderReranker,
)
from app.rag.vectorstores.qdrant_store import QdrantStore


class RetrievalService:

    def __init__(self):

        self.vector_store = QdrantStore()

        self.reranker = CrossEncoderReranker()

    def retrieve(
        self,
        question: str,
        k: int = 10,
    ) -> list[Document]:

        # Retrieve top-k documents using Hybrid Search
        documents = self.vector_store.similarity_search(
            query=question,
            k=k,
        )

        print(
            f"\nRetrieved {len(documents)} documents before reranking."
        )

        # Re-rank retrieved documents
        documents = self.reranker.rerank(
            query=question,
            documents=documents,
            top_k=3,
        )

        print(
            f"Returning {len(documents)} documents after reranking."
        )

        return documents