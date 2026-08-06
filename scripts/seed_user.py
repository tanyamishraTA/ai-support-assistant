import asyncio

from sqlalchemy import select

from app.auth.password import hash_password
from app.database.session import AsyncSessionLocal
from app.models.user import User, UserRole


USERS = [
    {
        "full_name": "Admin User",
        "email": "admin@example.com",
        "password": "Admin@123",
        "role": UserRole.ADMIN,
    },
    {
        "full_name": "John Employee",
        "email": "employee@example.com",
        "password": "Employee@123",
        "role": UserRole.EMPLOYEE,
    },
    {
        "full_name": "Guest User",
        "email": "guest@example.com",
        "password": "Guest@123",
        "role": UserRole.GUEST,
    },
]


async def seed_users():

    async with AsyncSessionLocal() as db:

        for user_data in USERS:

            result = await db.execute(
                select(User).where(
                    User.email == user_data["email"]
                )
            )

            existing_user = result.scalar_one_or_none()

            if existing_user:
                print(f"Skipping: {user_data['email']}")
                continue

            user = User(
                full_name=user_data["full_name"],
                email=user_data["email"],
                password_hash=hash_password(
                    user_data["password"]
                ),
                role=user_data["role"],
            )

            db.add(user)

        await db.commit()

    print("Users seeded successfully.")


if __name__ == "__main__":
    asyncio.run(seed_users())