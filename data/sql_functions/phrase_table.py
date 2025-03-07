import logging
from data.database_conn import get_session
from data.models.finnish_mod import finnish_phrases
from sqlalchemy import func


def get_finnish_phrase():
    try:
        session = get_session()
        phrase = session.query(finnish_phrases).order_by(func.random()).limit(1).first()
        session.close()
        return phrase
    except Exception as err:
        logging.exception(err)
        logging.error(f"Ошибка получения фразы: {err}")