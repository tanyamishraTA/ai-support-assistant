from sqlalchemy.ext.asyncio import AsyncSession

from app.models.ai_log import AILog
from app.repositories.ai_log_repository import (
    AILogRepository,
)


class AILogService:

    def __init__(
        self,
        db: AsyncSession,
    ):

        self.repository = AILogRepository(
            db
        )

    async def create_log(
        self,
        *,
        user_id: int,
        conversation_id: int,
        provider: str,
        prompt: str,
        response: str,
        latency: float,
        total_tokens: int = 0,
        estimated_cost: float = 0.0,
    ):

        log = AILog(
            user_id=user_id,
            conversation_id=conversation_id,
            provider=provider,
            prompt=prompt,
            response=response,
            latency=latency,
            total_tokens=total_tokens,
            estimated_cost=estimated_cost,
        )

        return await self.repository.create(
            log
        )