from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import User
from app.core.security import get_password_hash, verify_password

async def get_user_by_username(session: AsyncSession, username: str):
    """
    Fetch a user by username.
    """
    result = await session.execute(select(User).where(User.username == username))
    return result.scalar_one_or_none()

async def create_user(session: AsyncSession, user_data: dict): 
    """
    Create a new user.
    """
    hashed = get_password_hash(user_data["password"])
    user = User(
        username=user_data["username"],
        email=user_data["email"],
        hashed_password=hashed,
        is_admin=False
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

async def authenticate_user(session: AsyncSession, username: str, password: str):
    """
    Authenticate a user.
    """
    user = await get_user_by_username(session, username)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user