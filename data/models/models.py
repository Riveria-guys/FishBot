from sqlalchemy import Column, BigInteger, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    chat_id = Column(BigInteger)
    user_id = Column(BigInteger)
