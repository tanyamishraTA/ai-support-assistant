from sqlalchemy.ext.asyncio import AsyncSession

from app.models.conversation import Conversation
from app.models.message import Message, MessageRole
from app.repositories.conversation_repository import ConversationRepository
from app.repositories.message_repository import MessageRepository


class ConversationService:

    def __init__(
        self,
        db: AsyncSession,
    ):

        self.conversation_repository = (
            ConversationRepository(db)
        )

        self.message_repository = (
            MessageRepository(db)
        )

    async def create_conversation(
        self,
        user_id: int,
        title: str = "New Conversation",
    ) -> Conversation:

        conversation = Conversation(
            title=title,
            user_id=user_id,
        )

        return await self.conversation_repository.create(
            conversation
        )

    async def get_conversation(
        self,
        conversation_id: int,
    ):

        return await self.conversation_repository.get_by_id(
            conversation_id
        )

    async def get_history(
        self,
        conversation_id: int,
    ):

        return await self.message_repository.get_by_conversation(
            conversation_id
        )

    async def save_user_message(
        self,
        conversation_id: int,
        content: str,
    ):

        message = Message(
            conversation_id=conversation_id,
            role=MessageRole.USER,
            content=content,
        )

        return await self.message_repository.create(
            message
        )

    async def save_assistant_message(
        self,
        conversation_id: int,
        content: str,
    ):

        message = Message(
            conversation_id=conversation_id,
            role=MessageRole.ASSISTANT,
            content=content,
        )

        return await self.message_repository.create(
            message
        )