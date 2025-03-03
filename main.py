import telebot
import os
from dotenv import load_dotenv
from config.config import BOT_TOKEN


# Загрузка переменных окружения из файла .env
load_dotenv()

# Инициализация бота с использованием токена из config 

TOKEN = BOT_TOKEN
bot = telebot.TeleBot(TOKEN)

# Здесь были Максим, Женя , Коля , Денис и Лёва

# Отображение команд внутри бота
bot.set_my_commands([
    telebot.types.BotCommand("msp", "Магический шар"),
    telebot.types.BotCommand("start", "Запуск бота"),
    telebot.types.BotCommand("help", "Список команд"),
    telebot.types.BotCommand("finnish", "Финские фразы"),
])



# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Отправляет приветственное сообщение пользователю."""
    bot.reply_to(message, "Привет! Поздравляю все завелось")

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
