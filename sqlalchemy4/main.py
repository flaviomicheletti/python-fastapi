# from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
from models import Users, Base
from database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

# app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.get("/users/{user_id}")
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

session = SessionLocal()
result = session.query(Users.name).filter(Users.user_id == 1).first()
print(str(result[0]) == "User 1")
