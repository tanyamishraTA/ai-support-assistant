from sqlalchemy.ext.asyncio import AsyncSession

from app.models.document import DocumentStatus
from app.repositories.document_repository import DocumentRepository
from app.rag.chunking.semantic_chunker import SemanticChunkingService
from app.rag.embeddings.embedding_service import EmbeddingService
from app.rag.loaders.pdf_loader import PDFLoader
from app.rag.vectorstores.qdrant_store import QdrantStore



class IngestionService:

    def __init__(self, db: AsyncSession):

        self.document_repository = DocumentRepository(db)

        self.loader = PDFLoader()

        embeddings = EmbeddingService().get_embeddings()

        self.chunker = SemanticChunkingService(
            embeddings=embeddings
        )

        self.vector_store = QdrantStore()

    async def ingest_document(self, document_id: int,):

        document = await self.document_repository.get_by_id(
            document_id
        )

        if document is None:
            raise ValueError("Document not found")

        documents = self.loader.load(
            file_path=document.file_path,
            document_id=document.id,
            filename=document.filename,
        )

        chunks = self.chunker.chunk_documents(
            documents
        )

        self.vector_store.add_documents(
            chunks
        )

        document.status = DocumentStatus.INDEXED

        await self.document_repository.commit()

        return len(chunks)