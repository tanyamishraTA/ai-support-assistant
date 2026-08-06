from sqlalchemy import select

from app.models.message import Message

from .base_repository import BaseRepository


class MessageRepository(
    BaseRepository[Message]
):

    def __init__(self, db):

        super().__init__(
            db,
            Message,
        )

    async def get_by_conversation(
        self,
        conversation_id: int,
    ) -> list[Message]:

        result = await self.db.execute(
            select(Message)
            .where(
                Message.conversation_id == conversation_id
            )
            .order_by(Message.created_at.asc())
        )

        return list(result.scalars().all())