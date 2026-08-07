from enum import Enum

from pydantic import BaseModel, Field


class ConfidenceLevel(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Source(BaseModel):
    document: str
    page: int | None = None


class AIResponse(BaseModel):

    answer: str = Field(
        description="Answer to the user's question."
    )

    sources: list[Source] = []

    confidence: ConfidenceLevel