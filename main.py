import telebot
from config.config import BOT_TOKEN
from commands.init import register_all_handlers
from data.models.models import Base
from data.database_conn import engine

# Создание таблиц в базе данных
Base.metadata.create_all(engine)

# Инициализация бота с использованием токена из config 
bot = telebot.TeleBot(BOT_TOKEN)

# Здесь были Максим, Женя , Коля , Денис и Лёва

# Отображение команд внутри бота
bot.set_my_commands([
    telebot.types.BotCommand("msp", "Магический шар"),
    telebot.types.BotCommand("start", "Запуск бота"),
    telebot.types.BotCommand("help", "Список команд"),
    telebot.types.BotCommand("init", "Инициализация пользователя"),
])

# Регистрация всех обработчиков команд
register_all_handlers(bot)

# Запуск бота в режиме непрерывного прослушивания сообщений
print("Бот запущен...")

bot.polling(none_stop=True)
