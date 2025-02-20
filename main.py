import telebot
import random
import psycopg2
from psycopg2 import OperationalError
import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),  # IP сервера с БД (или localhost, если локально)
    "port": os.getenv("DB_PORT"),
}

def connect_db():
    """Создает подключение к БД и возвращает объект соединения и курсор."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
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
# Присвоение токена переменной окружения BOT_TOKEN
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

#Здесь был Максим
#Здесь был Женя
#Здесь был Денис

# Установка команд бота
bot.set_my_commands([
    telebot.types.BotCommand("msp", "Магический шар"),
    telebot.types.BotCommand("start", "Запуск бота"),
    telebot.types.BotCommand("help", "Список команд"),
])



# Обработчик команд /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Отправляет приветственное сообщение пользователю."""
    # bot.reply_to(message, "Привет! Я твой бот. Чем могу помочь?")

    conn, cursor = connect_db()
    if conn:
        cursor.execute("SELECT finnish FROM finish_phrases ORDER BY RANDOM() LIMIT 1;")

    bot.reply_to(message, cursor.fetchall())

# Обработчик команд /help
@bot.message_handler(commands=['help'])
def send_help(message):
    """Отправляет список команд пользователю."""
    bot.reply_to(message, "Тебе тут никто не поможет, сам разбирайся.\nВот список команд: \n/start - стартуем бота\n/help - список команд\n/msp - магический шар")

# Обработчик команд /msp (Magic Sphere)
@bot.message_handler(commands=['msp'])
def magic_sphere(message):
    """Волшебный шар"""
    answers = [
        "Бесспорно",
        "Предрешено",
        "Никаких сомнений",
        "Можешь быть уверен в этом",
        "Мне кажется — да",
        "Нет",
        "По моим данным — нет",
        "Весьма сомнительно",
        "Не думаю, что это хорошая идея",
        "Сконцентрируйся и спроси опять",
    ]
    bot.reply_to(message, f"🎱 {random.choice(answers)}")

# Обработчик всех входящих сообщений в личке и группах
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """Обрабатывает сообщения в личных чатах и группах."""
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
