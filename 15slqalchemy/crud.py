from sqlalchemy.orm import Session
import models


def get_user(db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.user_id == user_id).first()
