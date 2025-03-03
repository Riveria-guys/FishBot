from sqlalchemy import create_engine
from config.config import DATABASE_URL

engine_url = DATABASE_URL

def connect_db():
    engine = create_engine(engine_url, echo=True)
    with engine.connect() as connection:
        print("Успешное подключение к БД")
