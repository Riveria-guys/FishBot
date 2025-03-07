import logging
from data.sql_functions import get_finnish_phrase


# Обработчик команды /finnish
def register_finnish_phrases(bot):
    try:
        @bot.message_handler(commands=['finnish'])
        def finnish_phrases(message):
            phrase = get_finnish_phrase()
            bot.reply_to(message, f'Фраза: \n{phrase.phrase} \nПеревод: \n{phrase.translation}')
    except Exception as err:
        logging.exception(err)
        logging.error("Ошибка при регистрации обработчика команды /finnish")
        