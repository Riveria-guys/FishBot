from commands.handlers.base_hendlers import register_start, register_help
from commands.handlers.magic_ball import register_magic_sphere
from commands.handlers.initialization import register_init
from commands.handlers.finnish import register_finnish_phrases

def register_all_handlers(bot):
    register_start(bot)
    register_magic_sphere(bot)
    register_help(bot)
    register_init(bot)
    register_finnish_phrases(bot)