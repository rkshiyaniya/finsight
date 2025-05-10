from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.crud.transaction import get_transactions, create_transaction
from app.schemas import TransactionCreate, TransactionOut
from typing import List
from app.core.deps import get_current_user

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get("/{user_id}", response_model=List[TransactionOut])
async def list_transactions(user_id: str, session: AsyncSession = Depends(get_session)):
    """
    Fetch transactions for a specific user.
    """
    transactions = await get_transactions(session, user_id)
    return transactions

@router.post("/", response_model=TransactionOut)
async def add_transaction(txn: TransactionCreate, session: AsyncSession = Depends(get_session)):
    """
    Create a new transaction.
    """
    transaction = await create_transaction(session, txn.dict())
    return transaction

@router.get("/secure/me")
async def get_me(user=Depends(get_current_user)):
    return {"username": user.username, "admin": user.is_admin}
