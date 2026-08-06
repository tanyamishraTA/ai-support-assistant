from pathlib import Path

from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.document import Document
from app.rag.ingestion_service import IngestionService
from app.repositories.document_repository import DocumentRepository
from app.schemas.document import DocumentResponse
from app.storage.local_storage import LocalStorageService


class DocumentService:

    def __init__(
        self,
        db: AsyncSession,
    ):
        self.db = db

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

        # Create database record
        document = Document(
            filename=file.filename,
            stored_filename=stored_filename,
            file_path=file_path,
            file_size=Path(file_path).stat().st_size,
            mime_type=file.content_type,
            uploaded_by=uploaded_by,
        )

        document = await self.repository.create(
            document
        )

        # Automatically ingest into Qdrant
        ingestion_service = IngestionService(
            self.db
        )

        try:

            await ingestion_service.ingest_document(
                document.id
            )

        except Exception:

            document.status = document.status.FAILED

            await self.repository.commit()

            raise

        return DocumentResponse.model_validate(
            document
        )