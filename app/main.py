from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.middleware.exception_handler import (
    register_exception_handlers,
)

from app.api.document import router as document_router
from app.api import chat

app = FastAPI(
    title="AI Support Assistant",
    version="1.0.0",
)

register_exception_handlers(app)

app.include_router(auth_router)
app.include_router(document_router)
app.include_router(chat.router)


@app.get("/")
async def root():
    return {
        "message": "AI Support Assistant API"
    }