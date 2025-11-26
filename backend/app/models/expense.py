from sqlalchemy import Column,Integer, String, Float, Date, ForeignKey
from app.database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(255))
    amount = Column(Float)
    category = Column(String(255))
    date = Column(Date)
    note = Column(String(255))
    receipt_url = Column(String(255), nullable = True)