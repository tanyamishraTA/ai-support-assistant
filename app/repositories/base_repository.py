from typing import Generic, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):

    def __init__(
        self,
        db: AsyncSession,
        model: Type[ModelType],
    ):
        self.db = db
        self.model = model

    async def create(
        self,
        obj: ModelType,
    ) -> ModelType:

        self.db.add(obj)

        await self.db.commit()

        await self.db.refresh(obj)

        return obj

    async def get_by_id(
        self,
        obj_id: int,
    ) -> ModelType | None:

        result = await self.db.execute(
            select(self.model).where(
                self.model.id == obj_id
            )
        )

        return result.scalar_one_or_none()

    async def get_all(
        self,
    ) -> list[ModelType]:

        result = await self.db.execute(
            select(self.model)
        )

        return list(result.scalars().all())

    async def delete(
        self,
        obj: ModelType,
    ) -> None:

        await self.db.delete(obj)

        await self.db.commit()