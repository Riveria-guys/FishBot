import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
BOT_TOKEN = os.getenv("TOKEN")
if BOT_TOKEN is None:
    print("Ошибка: токен не найден!")
else:
    print("Токен успешно загружен.")