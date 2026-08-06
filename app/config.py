from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    DATABASE_URL: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    QDRANT_URL: str
    LLM_PROVIDER: str

    EMBEDDING_MODEL: str = "BAAI/bge-small-en-v1.5"

    QDRANT_URL: str
    QDRANT_API_KEY: str

    QDRANT_COLLECTION_NAME: str = "support_assistant"

    SPARSE_MODEL: str = "Qdrant/bm25"

    OLLAMA_MODEL: str = "llama3.2:latest"

    DEFAULT_LLM: str = "gemini"

    GEMINI_API_KEY: Optional[str] = None

    GEMINI_MODEL: str = "gemini-2.5-flash"

    DEFAULT_LLM: str = "ollama"

    

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()