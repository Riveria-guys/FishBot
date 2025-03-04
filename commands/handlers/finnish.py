from data.core import get_finnish_phrase

# ТУТ НИХУЯ НЕ РАБОТАЕТ Я ЕЩЕ НЕ ПЕРЕДЕЛАЛ ПОД НОВУЮ БИБЛИОТЕКУ


# Обработчик команды /finnish
def register_finnish_phrases(bot):
    @bot.message_handler(commands=['finnish'])
    def finnish_phrases(message):
        phrase = get_finnish_phrase()
        bot.reply_to(message, f'Фраза: \n{phrase.phrase} \nПеревод: \n{phrase.translation}')
        