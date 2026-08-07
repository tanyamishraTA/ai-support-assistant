from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.current_user import get_current_user
from app.database.session import get_db
from app.models.user import User
from app.schemas.conversation import (
    ConversationResponse,
    MessageResponse,
)
from app.services.conversation_service import ConversationService

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"],
)

@router.get(
    "",
    response_model=list[ConversationResponse],
)
async def get_conversations(
    current_user: User = Depends(
        get_current_user
    ),
    db: AsyncSession = Depends(
        get_db
    ),
):

    service = ConversationService(db)

    conversations = (
        await service.get_user_conversations(
            current_user.id
        )
    )

    return conversations

@router.get(
    "/{conversation_id}",
    response_model=list[MessageResponse],
)
async def get_messages(
    conversation_id: int,
    current_user: User = Depends(
        get_current_user
    ),
    db: AsyncSession = Depends(
        get_db
    ),
):

    service = ConversationService(db)

    conversation = await service.get_conversation(
    conversation_id
)

    if conversation is None:

        raise HTTPException(
            status_code=404,
            detail="Conversation not found.",
        )

    # Authorization check
    if conversation.user_id != current_user.id:

        raise HTTPException(
            status_code=403,
            detail="Access denied.",
        )

    return await service.get_history(
        conversation_id
    )

@router.delete(
    "/{conversation_id}",
)
async def delete_conversation(
    conversation_id: int,
    current_user: User = Depends(
        get_current_user
    ),
    db: AsyncSession = Depends(
        get_db
    ),
):

    service = ConversationService(db)

    conversation = await service.get_conversation(
    conversation_id)

    if conversation is None:

        raise HTTPException(
            status_code=404,
            detail="Conversation not found.",
        )

    # Authorization check
    if conversation.user_id != current_user.id:

        raise HTTPException(
            status_code=403,
            detail="Access denied.",
        )

    await service.delete_conversation(
        conversation_id
    )

    return {
        "message": "Conversation deleted successfully."
    }