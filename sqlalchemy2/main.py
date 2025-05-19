from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session, sessionmaker, declarative_base
from sqlalchemy import create_engine, Column, Integer, String

db_url = "postgresql://postgres:postgres@localhost:5438/postgres"
engine = create_engine(db_url)

LocalSession = sessionmaker(bind=engine)

Base = declarative_base()


class Users(Base):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String(80))

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


def get_session():
    session = LocalSession()
    try:
        yield session
    finally:
        session.close()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/{user_id}")
def read_item(user_id, session: Session = Depends(get_session)):
    return session.query(Users).filter(Users.user_id == user_id).first()


"""
uvicorn main:app --reload
"""