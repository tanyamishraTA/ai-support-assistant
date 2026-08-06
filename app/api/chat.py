from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.current_user import get_current_user
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
async def chat(
    request: ChatRequest,
    current_user: User = Depends(
        get_current_user
    ),
    db: AsyncSession = Depends(
        get_db
    ),
):

    service = ChatService(
        db=db,
        provider=request.provider,
    )

    response = await service.chat(
        user_id=current_user.id,
        question=request.question,
        conversation_id=request.conversation_id,
    )

    return ChatResponse(
        answer=response["answer"],
        conversation_id=response["conversation_id"],
    )