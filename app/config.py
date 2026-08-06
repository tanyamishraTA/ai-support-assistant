from pydantic_settings import BaseSettings, SettingsConfigDict


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
    

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()