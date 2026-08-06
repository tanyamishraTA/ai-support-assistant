from app.ai.ai_service import AIService
from app.ai.llm.base import LLMProvider
from app.rag.retrieval_service import RetrievalService


class RAGService:

    def __init__(
        self,
        provider: LLMProvider,
    ):

        self.retrieval_service = RetrievalService()

        self.ai_service = AIService(
            provider=provider,
        )

    def build_context(
        self,
        documents,
    ) -> str:

        context = []

        for document in documents:

            filename = document.metadata.get(
                "filename",
                "Unknown",
            )

            page = document.metadata.get(
                "page",
                "Unknown",
            )

            context.append(f""" 
            Document: {filename}
            Page: {page}
            {document.page_content}
"""
            )

        return "\n\n".join(context)

    def ask(
        self,
        question: str,
    ) -> str:

        documents = self.retrieval_service.retrieve(
            question=question,
        )

        context = self.build_context(
            documents,
        )

        return self.ai_service.generate_response(
            question=question,
            context=context,
        )