from sqlalchemy import select

from app.models.document import Document

from .base_repository import BaseRepository


class DocumentRepository(
    BaseRepository[Document]
):

    def __init__(self, db):
        super().__init__(
            db,
            Document,
        )

    async def get_by_filename(
        self,
        filename: str,
    ) -> Document | None:

        result = await self.db.execute(
            select(Document).where(
                Document.filename == filename
            )
        )

        return result.scalar_one_or_none()

    async def get_by_status(
        self,
        status,
    ) -> list[Document]:

        result = await self.db.execute(
            select(Document).where(
                Document.status == status
            )
        )

        return list(result.scalars().all())