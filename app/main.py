from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.api import chat
from app.api.auth import router as auth_router
from app.api.conversation import (
    router as conversation_router,
)
from app.api.document import (
    router as document_router,
)
from app.core.rate_limiter import limiter
from app.middleware.exception_handler import (
    register_exception_handlers,
)

app = FastAPI(
    title="AI Support Assistant",
    version="1.0.0",
)

# Register limiter
app.state.limiter = limiter

# Rate limit exception handler
app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler,
)

# Rate limit middleware
app.add_middleware(
    SlowAPIMiddleware,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom exception handlers
register_exception_handlers(app)

# Routers
app.include_router(auth_router)
app.include_router(document_router)
app.include_router(chat.router)
app.include_router(conversation_router)


@app.get("/")
async def root():
    return {
        "message": "AI Support Assistant API"
    }