from aiogram import Bot

from . commands_list import main_menu_commands


async def set_main_menu(bot: Bot):
    await bot.set_my_commands(main_menu_commands)
