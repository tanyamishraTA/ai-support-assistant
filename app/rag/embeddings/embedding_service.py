from langchain_huggingface import HuggingFaceEmbeddings

from app.core.config import settings


class EmbeddingService:
    """
    Singleton service for loading the embedding model.
    """

    _embeddings = None

    def __init__(self):
        if EmbeddingService._embeddings is None:

            EmbeddingService._embeddings = HuggingFaceEmbeddings(
                model_name=settings.EMBEDDING_MODEL,
                model_kwargs={
                    "device": "cpu",
                },
                encode_kwargs={
                    "normalize_embeddings": True,
                },
            )

    def get_embeddings(self):
        return EmbeddingService._embeddings