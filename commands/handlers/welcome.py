import random
from captcha.image import ImageCaptcha

captcha_dict = {}   

def register_welcome(bot):
 @bot.message_handler(content_types=['new_chat_members'])
 def welcome(message):
    for new_member in message.new_chat_members:
        user_id = new_member.id
        chat_id = message.chat.id

        if new_member.id == bot.get_me().id:
            bot.send_message(chat_id, "Всем привет, я ваш бот🤖, прошу любить и жаловать❤️!")
        else:
            bot.send_message(chat_id, f"Добро пожаловать, @{new_member.username}! Рады тебя видеть! "
                                      f"Будьте добры, изучите правила этого сообщества.")

            # Генерируем CAPTCHA
            captcha_text = str(random.randint(1000, 9999))
            image = ImageCaptcha()
            captcha = image.generate(captcha_text)

                # Ограничиваем права (можно писать только текст)
            bot.restrict_chat_member(
                    chat_id, user_id,
                    can_send_messages=True,
                    can_send_media_messages=False,
                    can_send_other_messages=False,
                    can_add_web_page_previews=False
                )

            # Отправляем
            bot.send_photo(chat_id, captcha, caption=f"@{new_member.username}, введи код с картинки, чтобы подтвердить, что ты не бот.")

                # Сохраняем ожидаемый ответ + счётчик попыток
            captcha_dict[user_id] = {"text": captcha_text, "chat_id": chat_id, "attempts": 0}

 @bot.message_handler(func=lambda message: message.chat.type in ["supergroup", "group"])
 def check_captcha(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    user_answer = message.text.strip()

    # Проверяем, есть ли пользователь в списке CAPTCHA
    if user_id in captcha_dict:
        correct_answer = captcha_dict[user_id]["text"]
        if user_answer == correct_answer:
            # Полностью снимаем ограничения
            bot.restrict_chat_member(
                chat_id, user_id,
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True
            )
            bot.send_message(chat_id, f"@{message.from_user.username}, добро пожаловать в группу! ✅ ")
            del captcha_dict[user_id]  # Убираем из списка
        else:
            captcha_dict[user_id]["attempts"] += 1  # Увеличиваем количество попыток
            if captcha_dict[user_id]["attempts"] >= 2:
                try:
                    # Кикаем пользователя
                    bot.kick_chat_member(chat_id, user_id)
                    bot.send_message(chat_id, f"🚫 @{message.from_user.username} кикнут за неправильный ввод CAPTCHA.")
                except Exception as e:
                    bot.send_message(chat_id, f"Ошибка при кике: {e}")
                del captcha_dict[user_id]  # Убираем пользователя из списка
            else:
                bot.send_message(chat_id, f"❌ Неверная каптча! У тебя осталась 1 попытка.")