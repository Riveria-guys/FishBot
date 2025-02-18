import telebot

# Инициализация бота с использованием токена
# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

# Обработчик команд /start и /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Отправляет приветственное сообщение пользователю."""
    bot.reply_to(message, "Привет! Я твой бот. Чем могу помочь?")

# Обработчик всех входящих сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """Эхо-функция, повторяет полученное сообщение."""
    bot.reply_to(message, message.text)

# Запуск бота в режиме непрерывного прослушивания сообщений
print("Бот запущен...")
bot.polling(none_stop=True)
