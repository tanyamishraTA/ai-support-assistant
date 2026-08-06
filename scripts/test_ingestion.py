import asyncio

from app.database.session import AsyncSessionLocal
from app.rag.ingestion_service import IngestionService


async def main():

    async with AsyncSessionLocal() as db:

        service = IngestionService(db)

        chunks = await service.ingest_document(
            document_id=1
        )

        print(f"Indexed {chunks} chunks")


if __name__ == "__main__":
    asyncio.run(main())