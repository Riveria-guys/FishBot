import telebot

def register_welcome(bot):
    @bot.message_handler(content_types=['new_chat_members'])
    def welcome(message):
        for new_member in message.new_chat_members:
            if new_member.id == bot.get_me().id:
                bot.send_message(message.chat.id, "Всем привет, я ваш бот🤖, прошу любить и жаловать❤️!")
            else:
                bot.send_message(message.chat.id, f"Добро пожаловать, @{new_member.username}!, рады тебя видеть! Будьте добры изучите правила этого сообщества.")