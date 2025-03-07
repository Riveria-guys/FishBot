import logging
import random
from captcha.image import ImageCaptcha

captcha_dict = {}   

def send_captcha(bot, chat_id, user_id):
    captcha_text = str(random.randint(1000, 9999))
    image = ImageCaptcha()
    captcha = image.generate(captcha_text)

    # Отправляем фото с CAPTCHA
    bot.send_photo(chat_id, captcha, caption=f"@{user_id}, введи код с картинки, чтобы подтвердить, что ты не бот.")
    
    # Сохраняем ожидаемый ответ и счётчик попыток
    captcha_dict[user_id] = {"text": captcha_text, "chat_id": chat_id, "attempts": 0}

def add_restrictions(bot, chat_id, user_id):
        bot.restrict_chat_member(
        chat_id, user_id,
        can_send_messages=True,
        can_send_media_messages=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False
    )

def remove_restrictions(bot, chat_id, user_id):
    bot.restrict_chat_member(
        chat_id, user_id,
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True
    )

def kick_user(bot, chat_id, user_id):
    try:
        # Кикаем пользователя
        bot.kick_chat_member(chat_id, user_id)
        bot.send_message(chat_id, f"🚫 @{message.from_user.username} кикнут за неправильный ввод CAPTCHA.")
    except Exception as e:
        bot.send_message(chat_id, f"Ошибка при кике: {e}")
        logging.exception(e)
        logging.error("Ошибка при кике пользователя")


def register_welcome(bot):
    @bot.message_handler(content_types=['new_chat_members'])
    def welcome(message):
        for new_member in message.new_chat_members:

            if new_member.id == bot.get_me().id:
                bot.send_message(message.chat.id, "Всем привет, я ваш бот🤖, прошу любить и жаловать❤️!")
            else:
                bot.send_message(message.chat.id, f"Добро пожаловать, @{new_member.username}! Рады тебя видеть! "
                                        f"Будьте добры, изучите правила этого сообщества.")
                
                # Ограничиваем пользователя
                add_restrictions(bot, message.chat.id, new_member.id)
                # Создаем и отправляем CAPTCHA
                send_captcha(bot, message.chat.id, new_member.id)

    @bot.message_handler(func=lambda message: message.from_user.id in captcha_dict)
    def check_captcha(message):
        user_id = message.from_user.id
        chat_id = message.chat.id
        user_answer = message.text.strip()
        correct_answer = captcha_dict[user_id]["text"]
            
        if user_answer == correct_answer:
            # Полностью снимаем ограничения
            remove_restrictions(bot, chat_id, user_id)

            del captcha_dict[user_id]

            bot.send_message(chat_id, f"@{message.from_user.username}, добро пожаловать в группу! ✅ ")
        
        else:
            captcha_dict[user_id]["attempts"] += 1  # Увеличиваем количество попыток
            if captcha_dict[user_id]["attempts"] >= 2:

                kick_user(bot, chat_id, user_id)
                del captcha_dict[user_id]  # Убираем пользователя из списка
            else:
                bot.send_message(chat_id, f"❌ Неверная каптча! У тебя осталась 1 попытка.")