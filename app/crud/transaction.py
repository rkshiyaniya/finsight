from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import Transaction

async def get_transactions(session: AsyncSession, user_id: str):    
    """
    Fetch transactions for a specific user.
    """
    result = await session.execute(select(Transaction).where(Transaction.user_id == user_id))
    transactions = result.scalars().all()
    return transactions

async def create_transaction(session: AsyncSession, txn_data: dict):
    """
    Create a new transaction.
    """
    transaction = Transaction(**txn_data)
    session.add(transaction)
    await session.commit()
    await session.refresh(transaction)
    return transaction