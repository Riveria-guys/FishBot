import telebot

# Инициализация бота с использованием токена
# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = "8099645779:AAHlgE9Bi36Xek7RssuHrFur3zEPbIpuKP8"
bot = telebot.TeleBot(TOKEN)

# Обработчик команд /start и /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Отправляет приветственное сообщение пользователю."""
    bot.reply_to(message, "Привет! Я твой бот. Чем могу помочь?")

# Обработчик всех входящих сообщений в личке и группах
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """Обрабатывает сообщения в личных чатах и группах."""
    if message.chat.type == "private":
        bot.reply_to(message, "Ты пишешь мне в личку!")
    elif message.chat.type in ["group", "supergroup"]:
        bot.reply_to(message, f"Сообщение в группе: {message.text}")

# Запуск бота в режиме непрерывного прослушивания сообщений
print("Бот запущен...")
bot.polling(none_stop=True)
