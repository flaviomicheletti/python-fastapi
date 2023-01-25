from sqlalchemy import Column, Integer, String

from database import Base


class Users(Base):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String(80))

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
