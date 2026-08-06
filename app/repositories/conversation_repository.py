from sqlalchemy import select

from app.models.conversation import Conversation
from .base_repository import BaseRepository


class ConversationRepository(
    BaseRepository[Conversation]
):

    def __init__(self, db):

        super().__init__(
            db,
            Conversation,
        )

    async def get_by_user(
        self,
        user_id: int,
    ) -> list[Conversation]:

        result = await self.db.execute(
            select(Conversation)
            .where(Conversation.user_id == user_id)
            .order_by(Conversation.created_at.desc())
        )

        return list(result.scalars().all())