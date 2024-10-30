from aiogram import Router
from . import admin_commands, user_commands


# function for assemling all routers
def get_routers() -> list[Router]:
    return [admin_commands.router, user_commands.router]
