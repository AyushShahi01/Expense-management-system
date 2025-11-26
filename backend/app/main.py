from fastapi import FastAPI
from app.routes import auth
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Expense API")

app.include_router(auth.router)
