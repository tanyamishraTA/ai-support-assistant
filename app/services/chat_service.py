import time

from sqlalchemy.ext.asyncio import AsyncSession

from app.ai.llm.base import LLMProvider
from app.rag.rag_service import RAGService
from app.services.ai_log_service import AILogService
from app.services.conversation_service import ConversationService
from app.services.intent_service import IntentService


class ChatService:

    def __init__(
        self,
        db: AsyncSession,
        provider: LLMProvider,
    ):

        self.provider = provider

        self.conversation_service = ConversationService(
            db
        )

        self.ai_log_service = AILogService(
            db
        )

        # Lazy initialization
        self.rag_service = None

    async def chat(
        self,
        *,
        user_id: int,
        question: str,
        conversation_id: int | None,
    ):

        # Create conversation if it doesn't exist
        if conversation_id is None:

            conversation = (
                await self.conversation_service.create_conversation(
                    user_id=user_id,
                )
            )

        else:

            conversation = (
                await self.conversation_service.get_conversation(
                    conversation_id
                )
            )

            if conversation is None:
                raise ValueError(
                    "Conversation not found."
                )

        # Load previous messages
        messages = (
            await self.conversation_service.get_history(
                conversation.id
            )
        )

        history = ""

        for message in messages:

            history += (
                f"{message.role.value}: "
                f"{message.content}\n"
            )

        # Save current user message
        await self.conversation_service.save_user_message(
            conversation.id,
            question,
        )

        # ---------------------------------
        # Handle greetings WITHOUT RAG
        # ---------------------------------
        if IntentService.is_small_talk(question):

            answer = {
                "answer": "Hello! 👋 How can I help you with your organization's documents today?",
                "sources": [],
            }

            await self.conversation_service.save_assistant_message(
                conversation.id,
                answer["answer"],
            )

            return {
                "conversation_id": conversation.id,
                "answer": answer["answer"],
                "sources": answer["sources"],
            }

        # ---------------------------------
        # Initialize RAG only when required
        # ---------------------------------
        if self.rag_service is None:

            self.rag_service = RAGService(
                provider=self.provider,
            )

        # ---------------------------------
        # Normal RAG pipeline
        # ---------------------------------

        start_time = time.perf_counter()

        response = self.rag_service.ask(
            question=question,
            history=history,
        )

        latency = (
            time.perf_counter() - start_time
        ) * 1000

        await self.conversation_service.save_assistant_message(
            conversation.id,
            response["answer"],
        )

        await self.ai_log_service.create_log(
            user_id=user_id,
            conversation_id=conversation.id,
            provider=self.provider.value,
            prompt=question,
            response=response["answer"],
            latency=latency,
            total_tokens=0,
            estimated_cost=0.0,
        )

        return {
            "conversation_id": conversation.id,
            "answer": response["answer"],
            "sources": response["sources"],
        }