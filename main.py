import telebot
import random
import psycopg2
from psycopg2 import OperationalError
import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

# -----------------------------------------------------------------------------------

def connect_db():
    """Создает подключение к БД через строку подключения и возвращает объект соединения и курсор."""
    try:
        conn = psycopg2.connect(DB_URL)  # Используем строку подключения напрямую
        cursor = conn.cursor()
        print("Подключение к БД успешно")
        return conn, cursor
    except OperationalError as e:
        print(f"Ошибка подключения: {e}")
        return None, None
    

def close_db(conn, cursor):
    """Закрывает соединение с БД."""
    if cursor:
        cursor.close()
    if conn:
        conn.close()
        print("Соединение закрыто")

# Инициализация бота с использованием токена
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

#Здесь был Максим
#Здесь был Женя
#Здесь был Денис
#Здесь был Лёва
#Здесь был Коля

# Отображение команд внутри бота
bot.set_my_commands([
    telebot.types.BotCommand("msp", "Магический шар"),
    telebot.types.BotCommand("start", "Запуск бота"),
    telebot.types.BotCommand("help", "Список команд"),
    telebot.types.BotCommand("finnish", "Финские фразы"),
])






# Обработчик всех входящих сообщений в личке и группах
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     """Обрабатывает сообщения в личных чатах и группах."""
    # Здесь 2 варианта обработки сообщений: в личных чатах и в группах
    # В первом случае бот отвечает на сообщение ТОЛЬКО в личке
    # Во втором случае бот отвечает на сообщение ТОЛЬКО в группе
    # if message.chat.type == "private":
    #     bot.reply_to(message, "Ты пишешь мне в личку!")
    # elif message.chat.type in ["group", "supergroup"]:
    #     bot.reply_to(message, f"Сообщение в группе: {message.text}")
    # Что бы оно нас не заебывало я закоментил что бы можно было использовать код для работы в дальнейшем


# Запуск бота в режиме непрерывного прослушивания сообщений
print("Бот запущен...")
bot.polling(none_stop=True)
