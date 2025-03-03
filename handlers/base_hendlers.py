#zdes obrobotka vseh zaprosov
import telebot


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Отправляет приветственное сообщение пользователю."""
    bot.reply_to(message, "Привет! Я твой бот. Чем могу помочь?")


# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    """Отправляет список команд пользователю."""
    bot.reply_to(message, "Тебе тут никто не поможет, сам разбирайся.\nВот список команд: \n/start - стартуем бота\n/help - список команд\n/msp - магический шар")
