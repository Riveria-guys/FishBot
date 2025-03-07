import logging


# Обработчик команды /start

def register_start(bot):
    try:
        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            """Отправляет приветственное сообщение пользователю."""
            bot.reply_to(message, "Привет! Я твой бот. Чем могу помочь?")
    except Exception as err:
        logging.exception(err)
        logging.error("Ошибка при регистрации обработчика команды /start")


# Обработчик команды /help
def register_help(bot):
    try:
        @bot.message_handler(commands=['help'])
        def send_help(message):
            """Отправляет список команд пользователю."""
            bot.reply_to(message, "Тебе тут никто не поможет, сам разбирайся.\nВот список команд: \n/start - стартуем бота\n/help - список команд\n/msp - магический шар")
    except Exception as err:
        logging.exception(err)
        logging.error("Ошибка при регистрации обработчика команды /help")
        
