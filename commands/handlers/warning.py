import re

from data.json_load.warnings_load import add_warning, remove_warning, get_warnings

def register_warning(bot):
    @bot.message_handler(commands=["warn"])
    def warn_handler(message):
        match_add = re.match(r'/warn\s+add\s+@(\w+)\s+"(.+)"', message.text)
        match_rm = re.match(r'/warn\s+rm\s+@(\w+)\s+(all|last|\d+)', message.text)
        match_list = re.match(r'/warn\s+list(?:\s+@(\w+))?', message.text)

        if match_add:
            username = "@" + match_add.group(1)
            reason = match_add.group(2)
            add_warning(username, reason)
            bot.reply_to(message, f"✅ Добавлено предупреждение для {username}: {reason}")

        elif match_rm:
            username = "@" + match_rm.group(1)
            mode = match_rm.group(2)
            if remove_warning(username, mode):
                bot.reply_to(message, f"✅ Предупреждения {username} обновлены ({mode})")
            else:
                bot.reply_to(message, f"⚠ У {username} нет предупреждений")

        elif match_list:
            username = match_list.group(1)
            if username:
                warnings = get_warnings("@" + username)
                if warnings:
                    bot.reply_to(message, f"⚠ Предупреждения {username}:\n" + "\n".join(warnings))
                else:
                    bot.reply_to(message, f"✅ У {username} нет предупреждений")
            else:
                users = get_warnings()
                if users:
                    response = "\n".join([f"{u['username']}: {len(u['warnings'])} предупреждений" for u in users])
                    bot.reply_to(message, "📜 Список всех предупреждений:\n" + response)
                else:
                    bot.reply_to(message, "✅ Нет пользователей с предупреждениями")

        else:
            bot.reply_to(message, "⚠ Используйте команды:\n"
                                "`/warn add @user \"причина\"` – добавить\n"
                                "`/warn rm @user all|last|N` – удалить\n"
                                "`/warn list [@user]` – список")


