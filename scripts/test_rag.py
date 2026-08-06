from app.ai.llm.base import LLMProvider
from app.rag.rag_service import RAGService


service = RAGService(
    provider=LLMProvider.OLLAMA,
)

response = service.ask(
    "What is the dress code for women?"
)

print(response)