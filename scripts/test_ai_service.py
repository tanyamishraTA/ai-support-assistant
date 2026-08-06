from app.ai.ai_service import AIService
from app.ai.llm.base import LLMProvider

context = """
Employees receive 20 paid leaves every calendar year.
Leave requests must be approved by the reporting manager.
"""

question = "How many paid leaves do employees receive?"

service = AIService(
    provider=LLMProvider.OLLAMA,
)

response = service.generate_response(
    question=question,
    context=context,
)

print(response)