from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TransactionBase(BaseModel):
    user_id: str = Field(..., example="user_123")
    amount: float = Field(..., gt=0, example=150.75)
    currency: str = Field(default="USD", example="USD")
    description: Optional[str] = Field(None, example="Test transaction")

class TransactionCreate(TransactionBase):
    """
    Schema for creating a new transaction.
    """
    pass

class TransactionOut(TransactionBase):
    """
    Schema for outputting a transaction.
    """
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True