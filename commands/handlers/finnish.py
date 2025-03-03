
# ТУТ НИХУЯ НЕ РАБОТАЕТ Я ЕЩЕ НЕ ПЕРЕДЕЛАЛ ПОД НОВУЮ БИБЛИОТЕКУ

# Обработчик команды /finnish
@bot.message_handler(commands=['finnish'])
def finish_phrases(message):
    """Отправляет приветственное сообщение пользователю."""
    conn, cursor = connect_db()
    if conn:
        cursor.execute("SELECT finnish FROM finish_phrases ORDER BY RANDOM() LIMIT 1;")

    bot.reply_to(message, cursor.fetchall())
    
    close_db(conn, cursor)