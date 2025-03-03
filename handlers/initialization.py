import telebot
from main import bot
from data.core import create_table, add_user, get_users

# @bot.message_handler(commands=['initiazation'])
def init(message):
    create_table()
    add_user(message.from_user.username, message.chat.id)
    user = get_users()
    bot.reply_to(message, f"Пользуватель {user.username} добавлен")