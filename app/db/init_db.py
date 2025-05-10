import asyncio
from app.db.session import engine
from app.db.models import Base

async def init_db():
    # Create the database tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    # Run the init_db function
    asyncio.run(init_db())