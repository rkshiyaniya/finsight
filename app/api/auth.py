from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import UserCreate, Token
from app.core.security import create_access_token
from app.db.session import get_session
from app.crud.user import authenticate_user
from app.core.config import ACCESS_TOKEN_EXPIRE

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=Token)
async def login(user: UserCreate, session: AsyncSession = Depends(get_session)):
    db_user = await authenticate_user(session, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token(subject=db_user.username, expires_delta=ACCESS_TOKEN_EXPIRE)
    return {"access_token": token, "token_type": "bearer"}
