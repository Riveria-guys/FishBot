from sqlalchemy import Column, BigInteger, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    chat_id = Column(BigInteger)
    user_id = Column(BigInteger)

class finnish_phrases(Base):
    __tablename__ = 'finnish_phrases'

    id = Column(Integer, primary_key=True)
    phrase = Column(String)
    translation = Column(String)
