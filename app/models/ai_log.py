from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database.base import Base


class AILog(Base):
    __tablename__ = "ai_logs"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    prompt: Mapped[str] = mapped_column(Text)

    response: Mapped[str] = mapped_column(Text)

    total_tokens: Mapped[int] = mapped_column(Integer)

    latency: Mapped[float] = mapped_column(Float)

    estimated_cost: Mapped[float] = mapped_column(Float)

    from sqlalchemy.sql import func

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    user = relationship(
        "User",
        back_populates="ai_logs"
    )