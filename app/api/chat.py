from fastapi import APIRouter, Depends

from app.ai.llm.base import LLMProvider
from app.auth.current_user import get_current_user
from app.models.user import User
from app.rag.rag_service import RAGService
from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
)

router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"],
)


@router.post(
    "",
    response_model=ChatResponse,
)
async def chat(
    request: ChatRequest,
    current_user: User = Depends(get_current_user),
):

    rag_service = RAGService(
        provider=request.provider,
    )

    answer = rag_service.ask(
        question=request.question,
    )

    return ChatResponse(
        answer=answer,
    )