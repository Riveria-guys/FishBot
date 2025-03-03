import random


# Обработчик командs /msp (Magic Sphere)
def register_magic_sphere (bot):
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
