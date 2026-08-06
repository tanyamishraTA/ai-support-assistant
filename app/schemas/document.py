from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.document import DocumentStatus


class DocumentResponse(BaseModel):
    id: int
    filename: str
    stored_filename: str
    file_path: str
    file_size: int
    mime_type: str
    status: DocumentStatus
    uploaded_by: int
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


class DocumentListResponse(BaseModel):
    documents: list[DocumentResponse]