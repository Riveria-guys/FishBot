import os
import logging
from dotenv import load_dotenv

try:
    load_dotenv()
except Exception as err:
    logging.exception(err)
    logging.error("Ошибка при загрузке файла .env")

DATABASE_URL = os.getenv("DATABASE_URL")
BOT_TOKEN = os.getenv("TOKEN")
