from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import DATABASE_URL

engine_url = DATABASE_URL

engine = create_engine(engine_url, echo=False)

Session = sessionmaker(bind=engine)

def get_session():
    return Session()
