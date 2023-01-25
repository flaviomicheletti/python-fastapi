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


# def get_session():
#     session = LocalSession()
#     try:
#         yield session
#     finally:
#         session.close()

# print(Depends)
# session = Session(Depends(get_session))
# print(session.query(Users).filter(Users.user_id == 1).first())

session = LocalSession()
result = session.query(Users.name).filter(Users.user_id == 1).first()
print(str(result[0]) == "User 1")
