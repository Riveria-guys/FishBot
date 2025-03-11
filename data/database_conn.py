import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import DATABASE_URL

engine_url = DATABASE_URL
try:
    engine = create_engine(engine_url, echo=True)
except Exception as err:
    logging.exception(err)
    logging.error("Ошибка при создании подключения к базе данных")

try:
    Session = sessionmaker(bind=engine)
except Exception as err:
    logging.exception(err)
    logging.error("Ошибка при создании сессии")
    
def get_session():
    return Session()
