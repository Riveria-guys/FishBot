import logging
from data.sql_functions.user_table import add_user

# Обработчик команды /init
def register_init(bot):
    try:
        @bot.message_handler(commands=['init'])
        def init(message):
            res_mess = add_user(message.from_user.username, message.chat.id, message.from_user.id)
            bot.reply_to(message, res_mess)
    except Exception as err:
        logging.exception(err)
        logging.error("Ошибка при регистрации обработчика команды /init")

