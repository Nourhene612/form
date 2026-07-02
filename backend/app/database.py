import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base  # important : importer Base ici pour qu'Alembic la trouve

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:useruser123@db:5432/database")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dépendance FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()