import json
import logging
from data.database_conn import get_session
from data.models.finnish_mod import finnish_phrases

def import_phrases_from_json():
    try:
        # Открываем и загружаем данные из файла JSON
        with open('data/json_load/json/phrases.json', 'r', encoding='utf-8') as file:
            phrases_data = json.load(file)
        
        session = get_session()
        
        # Проходим по каждой фразе в списке и добавляем её в базу данных
        for item in phrases_data:
            phrase = item['phrase']
            translation = item['translation']
            
            # Проверяем, существует ли уже эта фраза в базе данных
            existing_phrase = session.query(finnish_phrases).filter_by(phrase=phrase).first()
            if not existing_phrase:
                new_phrase = finnish_phrases(phrase=phrase, translation=translation)
                session.add(new_phrase)
        
        session.commit()
        session.close()    
    except Exception as e:
        logging.exception(e)
        logging.error("Ошибка при импорте фраз из JSON")
