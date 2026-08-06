from pathlib import Path

from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.document import Document
from app.repositories.document_repository import DocumentRepository
from app.schemas.document import DocumentResponse
from app.storage.local_storage import LocalStorageService


class DocumentService:

    def __init__(
        self,
        db: AsyncSession,
    ):
        self.repository = DocumentRepository(db)
        self.storage = LocalStorageService()

    async def upload_document(
        self,
        file: UploadFile,
        uploaded_by: int,
    ) -> DocumentResponse:

        # Save file locally
        stored_filename, file_path = await self.storage.save_file(
            file
        )

        # Create database object
        document = Document(
            filename=file.filename,
            stored_filename=stored_filename,
            file_path=file_path,
            file_size=Path(file_path).stat().st_size,
            mime_type=file.content_type,
            uploaded_by=uploaded_by,
        )

        # Save metadata
        document = await self.repository.create(
            document
        )

        return DocumentResponse.model_validate(
            document
        )