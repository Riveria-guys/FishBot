from telegram import Update
from telegram.ext import CallbackContext

rules_dict = {}

def rules(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    rules_text = rules_dict.get(chat_id, "Правила не установлены.")
    update.message.reply_text(rules_text)

def add_rules(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    new_rules = ' '.join(context.args)
    if new_rules:
        rules_dict[chat_id] = new_rules
        update.message.reply_text(f"Правила обновлены: {new_rules}")
    else:
        update.message.reply_text("Введите правила для добавления.")
