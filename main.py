import logging
from loggers import setup_logging

setup_logging()
logger = logging.getLogger("my_logger")

import telebot
from config.config import BOT_TOKEN
from commands.init import register_all_handlers
from data.models.models import Base
from data.database_conn import engine
from data.json_load.all_load import import_all_data


logging.info("Бот запущен...")

# Создание таблиц в базе данных
Base.metadata.create_all(engine)


# Импорт всех данных из JSON в базу данных
import_all_data()

# Инициализация бота с использованием токена из config 
bot = telebot.TeleBot(BOT_TOKEN)

# Здесь были Максим, Женя , Коля , Денис и Лёва

# Отображение команд внутри бота
bot.set_my_commands([
    telebot.types.BotCommand("msp", "Магический шар"),
    telebot.types.BotCommand("start", "Запуск бота"),
    telebot.types.BotCommand("help", "Список команд"),
    telebot.types.BotCommand("init", "Инициализация пользователя"),
    telebot.types.BotCommand("finnish", "Финские фразы"),
    telebot.types.BotCommand("warp", "предупреждения"),
])

# Регистрация всех обработчиков команд
register_all_handlers(bot)

# Запуск бота в режиме непрерывного прослушивания сообщений
print("Бот запущен...")


bot.polling(none_stop=True)
