from aiogram import Router
from . import admin_commands, user_commands, user_callback_handlers


# function for assemling all routers
def get_commands_routers() -> list[Router]:
    return [admin_commands.router, user_commands.router, user_callback_handlers.router]
