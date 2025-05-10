import asyncio
from app.db.session import AsyncSessionLocal
from app.db.models import User
from app.core.security import get_password_hash

async def create_admin():
    async with AsyncSessionLocal() as session:
        hashed_pw = get_password_hash("secret123")
        admin = User(
            username="admin",
            email="admin@finsight.com",
            hashed_password=hashed_pw,
            is_admin=True
        )
        session.add(admin)
        await session.commit()
        print("✅ Admin created")

if __name__ == "__main__":
    asyncio.run(create_admin())
