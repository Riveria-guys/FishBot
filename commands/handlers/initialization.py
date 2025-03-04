from data.core import add_user, get_users

def register_init(bot):
    @bot.message_handler(commands=['init'])
    def init(message):
        res_mess = add_user(message.from_user.username, message.chat.id, message.from_user.id)
        bot.reply_to(message, res_mess)