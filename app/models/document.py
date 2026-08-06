from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey, String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database.base import Base


class DocumentStatus(str, Enum):
    UPLOADED = "uploaded"
    PROCESSING = "processing"
    INDEXED = "indexed"
    FAILED = "failed"


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True)

    # Original filename uploaded by admin
    filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    # Unique filename stored on disk
    stored_filename: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    # Complete local path
    file_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    # Size in bytes
    file_size: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    # MIME type
    mime_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    # Upload / Processing status
    status: Mapped[DocumentStatus] = mapped_column(
        SQLEnum(DocumentStatus),
        default=DocumentStatus.UPLOADED,
        nullable=False,
    )

    uploaded_by: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    uploaded_by_user = relationship(
        "User",
        back_populates="uploaded_documents",
    )