from sqlalchemy import Column, Integer, String
from data.models.models import Base


class finnish_phrases(Base):
    __tablename__ = 'finnish_phrases'

    id = Column(Integer, primary_key=True)
    phrase = Column(String)
    translation = Column(String)
