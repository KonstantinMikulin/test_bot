from aiogram import Router
from .admin_commands import admin_router
from .user_commands import user_router
from .user_callback_handlers import user_callback_router
from .user_measurments_cmds import user_measure_router

__all__ = ["admin_router", "user_router", "user_measure_router", "user_callback_router"]


# function for assemling all routers
def get_commands_routers() -> list[Router]:
    return [admin_router, user_router, user_measure_router, user_callback_router]
