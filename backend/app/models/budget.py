from sqlalchemy import Column, Integer, Float, ForeignKey
from app.database import Base

class Budget(Base):
    __tablename__ = "Budgets"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("user.id"))
    amount = Column(Float)
    month = Column(Integer)
    year = Column(Integer)