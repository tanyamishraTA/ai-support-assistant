from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User


class UserRepository:

    @staticmethod
    async def create(
        db: AsyncSession,
        user: User,
    ) -> User:
        """
        Create a new user.
        """

        db.add(user)

        await db.commit()

        await db.refresh(user)

        return user

    @staticmethod
    async def get_by_email(
        db: AsyncSession,
        email: str,
    ) -> User | None:
        """
        Get user by email.
        """

        result = await db.execute(
            select(User).where(User.email == email)
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        user_id: int,
    ) -> User | None:
        """
        Get user by id.
        """

        result = await db.execute(
            select(User).where(User.id == user_id)
        )

        return result.scalar_one_or_none()

    @staticmethod
    async def get_all(
        db: AsyncSession,
    ) -> list[User]:
        """
        Get all users.
        """

        result = await db.execute(
            select(User)
        )

        return list(result.scalars().all())

    @staticmethod
    async def delete(
        db: AsyncSession,
        user: User,
    ) -> None:
        """
        Delete user.
        """

        await db.delete(user)

        await db.commit()