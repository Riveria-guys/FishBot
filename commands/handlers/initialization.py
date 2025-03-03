from data.core import add_user, get_users

def register_init(bot):
    @bot.message_handler(commands=['init'])
    def init(message):
        add_user(message.from_user.username, message.chat.id)
        user = get_users()
        bot.reply_to(message, f"Пользователь {user.username} добавлен")