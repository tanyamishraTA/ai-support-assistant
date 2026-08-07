from datetime import datetime

from pydantic import BaseModel

from app.models.message import MessageRole


class ConversationResponse(BaseModel):
    id: int
    title: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }


class MessageResponse(BaseModel):
    id: int
    role: MessageRole
    content: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }