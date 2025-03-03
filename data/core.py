from data.database_conn import engine, get_session
from data.models.models import User, Base


def create_table():
    try:
        Base.metadata.create_all(engine)
        print("Таблицы созданы")
    except Exception as e:
        print(f"Ошибка создания таблиц: {e}")


def add_user(username, chat_id):
    try:
        session_add = get_session()
        existing_user = session_add.query(User).filter_by(chat_id=chat_id).first()
        if existing_user:
            existing_user.username = username
            session_add.commit()
            print("Пользователь обновлен")
        else:
            new_user = User(username=username, chat_id=chat_id)
            session_add.add(new_user)
            session_add.commit()
            print("Пользователь добавлен")
        
        session_add.close()
    
    except Exception as e:
        print(f"Ошибка добавления пользователя: {e}")


def get_users():
    try:
        session = get_session()
        user = session.query(User).first()
        session.close()
        return user
    except Exception as e:
        print(f"Ошибка получения пользователя: {e}")
