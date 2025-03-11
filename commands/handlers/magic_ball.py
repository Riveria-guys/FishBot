import random
import logging

# Обработчик командs /msp (Magic Sphere)
def register_magic_sphere (bot):
    try:
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
    except Exception as err:
        logging.exception(err)
        logging.error("Ошибка при регистрации обработчика команды /msp")