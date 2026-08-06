from langchain_experimental.text_splitter import SemanticChunker
from langchain_core.documents import Document


class SemanticChunkingService:

    def __init__(
        self,
        embeddings,
    ):

        self.chunker = SemanticChunker(
            embeddings=embeddings,
            breakpoint_threshold_type="percentile",
        )

    def chunk_documents(
        self,
        documents: list[Document],
    ) -> list[Document]:

        return self.chunker.split_documents(
            documents
        )