from langchain_google_genai import ChatGoogleGenerativeAI

from app.core.config import settings


class GeminiService:

    _llm = None

    def __init__(self):

        if GeminiService._llm is None:

            GeminiService._llm = ChatGoogleGenerativeAI(
                model=settings.GEMINI_MODEL,
                google_api_key=settings.GEMINI_API_KEY,
                temperature=0.2,
            )

    def get_llm(self):

        return GeminiService._llm