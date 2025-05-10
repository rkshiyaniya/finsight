from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.crud.transaction import get_transactions, create_transaction

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get("/{user_id}")
async def list_transactions(user_id: str, session: AsyncSession = Depends(get_session)):
    """
    Fetch transactions for a specific user.
    """
    transactions = await get_transactions(session, user_id)
    return transactions

@router.post("/")
async def add_transaction(txn_data: dict, session: AsyncSession = Depends(get_session)):
    """
    Create a new transaction.
    """
    transaction = await create_transaction(session, txn_data)
    return transaction