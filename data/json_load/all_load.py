from data.json_load.phrases_load import import_phrases_from_json

def import_all_data():
    import_phrases_from_json()
    print("Все данные успешно импортированы в базу данных.")