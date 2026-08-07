from app.models.ai_log import AILog

from .base_repository import BaseRepository


class AILogRepository(
    BaseRepository[AILog]
):

    def __init__(self, db):

        super().__init__(
            db,
            AILog,
        )