import telebot
from config import TOKEN  # Импортируем токен

bot = telebot.TeleBot(TOKEN)  # Создаем объект бота

# Обработчик для команды /rules
@bot.message_handler(commands=['rules'])
def rules(message):
    bot.send_message(message.chat.id, "These are the group rules...")

# Обработчик для команды /addrules
@bot.message_handler(commands=['addrules'])
def add_rules(message):
    bot.send_message(message.chat.id, "Adding new rules...")
