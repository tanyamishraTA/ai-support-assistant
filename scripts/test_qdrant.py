from app.rag.loaders.pdf_loader import PDFLoader
from app.rag.chunking.semantic_chunker import SemanticChunkingService
from app.rag.embeddings.embedding_service import EmbeddingService
from app.rag.vectorstores.qdrant_store import QdrantStore


loader = PDFLoader()

documents = loader.load(
    file_path="data/uploads/b1418d6e-31cd-4931-872c-2a8cdac16b9b.pdf",
    document_id=1,
    filename="sample.pdf",
)

embeddings = EmbeddingService().get_embeddings()

chunker = SemanticChunkingService(
    embeddings
)

chunks = chunker.chunk_documents(
    documents
)

store = QdrantStore()

store.add_documents(
    chunks
)

print(
    f"Indexed {len(chunks)} chunks."
)