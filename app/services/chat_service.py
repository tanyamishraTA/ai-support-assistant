from sqlalchemy.ext.asyncio import AsyncSession

from app.ai.llm.base import LLMProvider
from app.rag.rag_service import RAGService
from app.services.conversation_service import ConversationService


class ChatService:

    def __init__(
        self,
        db: AsyncSession,
        provider: LLMProvider,
    ):

        self.conversation_service = ConversationService(db)

        self.rag_service = RAGService(
            provider=provider,
        )

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

        # Ask RAG
        response = self.rag_service.ask(
            question=question,
            history=history,
        )

        await self.conversation_service.save_assistant_message(
            conversation.id,
            response["answer"],
        )

        return {
            "conversation_id": conversation.id,
            "answer": response["answer"],
            "sources": response["sources"],
        }