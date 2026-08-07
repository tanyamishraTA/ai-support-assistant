from sqlalchemy.ext.asyncio import AsyncSession

from app.models.security_log import (
    SecurityEvent,
    SecurityLog,
)
from app.repositories.security_log_repository import (
    SecurityLogRepository,
)


class SecurityLogService:

    def __init__(
        self,
        db: AsyncSession,
    ):

        self.repository = SecurityLogRepository(
            db
        )

    async def log(
        self,
        *,
        event: SecurityEvent,
        endpoint: str,
        details: str,
        user_id: int | None = None,
        ip_address: str | None = None,
    ):

        log = SecurityLog(
            user_id=user_id,
            event=event,
            endpoint=endpoint,
            details=details,
            ip_address=ip_address,
        )

        await self.repository.create(
            log
        )