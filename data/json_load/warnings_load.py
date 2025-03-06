import json
import os


FOLDER_PATH = "data/json_load/json"
FILENAME = os.path.join(FOLDER_PATH, "warning_list.json")

def load_data():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Функция для сохранения данных
def save_data(data):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Функция для добавления предупреждения
def add_warning(username, reason):
    users = load_data()

    for user in users:
        if user["username"] == username:
            user["warnings"].append(reason)
            break
    else:
        users.append({"username": username, "warnings": [reason]})

    save_data(users)

# Функция для удаления предупреждений
def remove_warning(username, mode):
    users = load_data()

    for user in users:
        if user["username"] == username:
            if mode == "all":
                user["warnings"] = []
            elif mode == "last":
                if user["warnings"]:
                    user["warnings"].pop()
            elif mode.isdigit():
                index = int(mode) - 1
                if 0 <= index < len(user["warnings"]):
                    del user["warnings"][index]

            save_data(users)
            return True

    return False

# Функция для получения предупреждений
def get_warnings(username=None):
    users = load_data()

    if username:
        for user in users:
            if user["username"] == username:
                return user["warnings"]
        return None
    else:
        return users