from app.models.security_log import SecurityLog

from .base_repository import BaseRepository


class SecurityLogRepository(
    BaseRepository[SecurityLog]
):

    def __init__(self, db):

        super().__init__(
            db,
            SecurityLog,
        )