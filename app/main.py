from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db

app = FastAPI(
    title="AI Support Assistant",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {
        "message": "AI Support Assistant API is running"
    }


@app.get("/health/db")
async def database_health(
    db: AsyncSession = Depends(get_db),
):
    await db.execute(text("SELECT 1"))

    return {
        "database": "connected"
    }