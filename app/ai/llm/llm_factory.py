from app.ai.llm.base import LLMProvider
from app.ai.llm.gemini_service import GeminiService
from app.ai.llm.ollama_service import OllamaService


class LLMFactory:

    @staticmethod
    def get_llm(
        provider: LLMProvider,
    ):

        if provider == LLMProvider.GEMINI:
            return GeminiService().get_llm()

        if provider == LLMProvider.OLLAMA:
            return OllamaService().get_llm()

        raise ValueError(
            f"Unsupported LLM provider: {provider}"
        )