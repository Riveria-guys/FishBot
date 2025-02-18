import telebot
import random


# Инициализация бота с использованием токена
# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = "8099645779:AAHlgE9Bi36Xek7RssuHrFur3zEPbIpuKP8"
bot = telebot.TeleBot(TOKEN)

# Обработчик команд /start и /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Отправляет приветственное сообщение пользователю."""
    bot.reply_to(message, "Привет! Я твой бот. Чем могу помочь?")

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

# Обработчик всех входящих сообщений в личке и группах
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """Обрабатывает сообщения в личных чатах и группах."""
    # if message.chat.type == "private":
    #     bot.reply_to(message, "Ты пишешь мне в личку!")
    # elif message.chat.type in ["group", "supergroup"]:
    #     bot.reply_to(message, f"Сообщение в группе: {message.text}")
    # Что бы оно нас не заебывало я закоментил что бы можно было использовать код для работы в дальнейшем


# Запуск бота в режиме непрерывного прослушивания сообщений
print("Бот запущен...")
bot.polling(none_stop=True)
