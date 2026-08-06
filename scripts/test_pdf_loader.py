from app.rag.loaders.pdf_loader import PDFLoader

loader = PDFLoader()

documents = loader.load(
    file_path="data/uploads/51c3fffa-7a67-4913-855a-74d27d8dae05.pdf",
    document_id=1,
    filename="sample.pdf",
)

print(f"Pages Loaded: {len(documents)}")

print()

print(documents[0].metadata)

print()

print(documents[0].page_content[:500])