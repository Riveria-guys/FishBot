from sqlalchemy import Column, BigInteger, Integer, String
from data.models.models import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    chat_id = Column(BigInteger)
    user_id = Column(BigInteger)