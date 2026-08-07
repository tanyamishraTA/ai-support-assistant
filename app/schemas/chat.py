from pydantic import BaseModel, Field

from app.ai.llm.base import LLMProvider


class SourceResponse(BaseModel):
    document: str
    page: int | None = None


class ChatRequest(BaseModel):

    question: str = Field(
        min_length=1,
        max_length=2000,
    )

    provider: LLMProvider = LLMProvider.OLLAMA

    conversation_id: int | None = None


class ChatResponse(BaseModel):

    conversation_id: int

    answer: str

    sources: list[SourceResponse]