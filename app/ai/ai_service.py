from app.ai.llm.base import LLMProvider
from app.ai.llm.llm_factory import LLMFactory
from app.ai.prompts.chat_prompt import chat_prompt


class AIService:

    def __init__(
        self,
        provider: LLMProvider,
    ):

        self.llm = LLMFactory.get_llm(
            provider
        )

    def generate_response(
        self,
        question: str,
        context: str,
        history: str,
    ) -> str:

        prompt = chat_prompt.invoke(
            {
                "question": question,
                "context": context,
                "history": history,
            }
        )

        response = self.llm.invoke(
            prompt
        )

        return response.content