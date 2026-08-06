import asyncio

from scripts.seed_user import seed_users


async def seed():

    print("Seeding users...")
    await seed_users()

    print("Database seeded successfully.")


if __name__ == "__main__":
    asyncio.run(seed())