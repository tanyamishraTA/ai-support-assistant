from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.current_user import get_current_user
from app.core.rate_limiter import limiter
from app.database.session import get_db
from app.models.user import User
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "",
    response_model=ChatResponse,
)
@limiter.limit("30/minute")
async def chat(
    request: Request,
    payload: ChatRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):

    service = ChatService(
        db=db,
        provider=payload.provider,
    )

    return await service.chat(
        user_id=current_user.id,
        question=payload.question,
        conversation_id=payload.conversation_id,
    )