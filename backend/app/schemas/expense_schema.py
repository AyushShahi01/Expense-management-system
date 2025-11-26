from pydantic import BaseModel
from datetime import date

class ExpenseBase(BaseModel):
    title: str
    amount: float
    category: str
    date: date
    note: str | None = None

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseResponse(ExpenseBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True