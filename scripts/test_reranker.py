from app.rag.retrieval_service import RetrievalService

retriever = RetrievalService()

documents = retriever.retrieve(
    "What is the referral incentive for employees with 5 years of experience?"
)

print("\n===== Final Retrieved Documents =====")

for i, document in enumerate(documents, start=1):

    print(f"\nDocument {i}")
    print(document.metadata)
    print(document.page_content[:300])