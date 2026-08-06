import fitz

from langchain_core.documents import Document


class PDFLoader:

    def load(
        self,
        file_path: str,
        document_id: int,
        filename: str,
    ) -> list[Document]:

        pdf = fitz.open(file_path)

        documents = []

        try:
            for page_number, page in enumerate(pdf):

                text = page.get_text().strip()

                if not text:
                    continue

                documents.append(
                    Document(
                        page_content=text,
                        metadata={
                            "document_id": document_id,
                            "filename": filename,
                            "page": page_number + 1,
                            "source": file_path,
                        },
                    )
                )

        finally:
            pdf.close()

        return documents