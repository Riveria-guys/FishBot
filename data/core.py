from data.database_conn import get_session
from data.models.user_mod import User
from data.models.finnish_mod import finnish_phrases
from sqlalchemy import func


def add_user(username, chat_id, user_id):
    try:
        session = get_session()
        existing_user = session.query(User).filter(User.chat_id == chat_id).first()
        if existing_user:
            existing_user.username = username
            session.commit()
            res_mess = f"Пользователь {username} обновлен"
            session.close()
            return res_mess
        else:
            new_user = User(username=username, chat_id=chat_id, user_id=user_id)
            session.add(new_user)
            session.commit()
            res_mess = f"Пользователь {username} добавлен"
            session.close()
            return res_mess
    
    except Exception as e:
        print(f"Ошибка добавления пользователя: {e}")


def get_users(message):
    try:
        session = get_session()
        user = session.query(User).filter(User.chat_id == message.chat.id).first()
        session.close()
        return user
    except Exception as e:
        print(f"Ошибка получения пользователя: {e}")

def get_finnish_phrase():
    try:
        session = get_session()
        phrase = session.query(finnish_phrases).order_by(func.random()).limit(1).first()
        session.close()
        return phrase
    except Exception as e:
        print(f"Ошибка получения фразы: {e}")