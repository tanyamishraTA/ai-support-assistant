from sentence_transformers import CrossEncoder


class CrossEncoderReranker:

    def __init__(self):

        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    def rerank(
        self,
        query: str,
        documents: list,
        top_k: int = 3,
    ):

        if not documents:
            return []

        sentence_pairs = [
            (
                query,
                document.page_content,
            )
            for document in documents
        ]

        scores = self.model.predict(
            sentence_pairs
        )

        ranked_documents = sorted(
            zip(documents, scores),
            key=lambda x: x[1],
            reverse=True,
        )

        return [
            document
            for document, score in ranked_documents[:top_k]
        ]