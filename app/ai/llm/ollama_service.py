from langchain_ollama import ChatOllama

from app.config import settings


class OllamaService:

    _llm = None

    def __init__(self):

        if OllamaService._llm is None:

            OllamaService._llm = ChatOllama(
                model=settings.OLLAMA_MODEL,
                temperature=0.2,
            )

    def get_llm(self):

        return OllamaService._llm