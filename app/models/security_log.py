from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database.base import Base


class SecurityEvent(str, Enum):
    INVALID_TOKEN = "INVALID_TOKEN"
    ACCESS_DENIED = "ACCESS_DENIED"
    LOGIN_FAILED = "LOGIN_FAILED"
    PROMPT_INJECTION = "PROMPT_INJECTION"
    CONVERSATION_ACCESS_DENIED = "CONVERSATION_ACCESS_DENIED"
    DOCUMENT_UPLOAD_DENIED = "DOCUMENT_UPLOAD_DENIED"


class SecurityLog(Base):
    __tablename__ = "security_logs"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True,
    )

    event: Mapped[SecurityEvent] = mapped_column(
        SQLEnum(SecurityEvent)
    )

    endpoint: Mapped[str] = mapped_column(
        String(255)
    )

    details: Mapped[str] = mapped_column(
        Text
    )

    ip_address: Mapped[str | None] = mapped_column(
        String(45),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    user = relationship(
        "User",
        back_populates="security_logs",
    )