import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@db/postgres"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

###

from sqlalchemy import Column, Integer, String


class Users(Base):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String(80))

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


###

from sqlalchemy.orm import Session


def get(db_session: Session, id: int):
    return db_session.query(Users).filter(Users.user_id == id).first()

###

# from app.db import SessionLocal

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

get(get_db(), 1)
