import asyncio
import logging

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from bot.filters import IsAdminFilter

logger = logging.getLogger(__name__)

# creating router`s onject
admin_router = Router(name="admin router")


@admin_router.message(CommandStart(), IsAdminFilter())
async def cmd_admin_start(message: Message, some_new):
    logger.info("Enter admin`s /start handler")
    logger.info(f"This is info from inner middleware: '{some_new}'")
    
    await message.answer('Admin, you sent /start! Welcome!')
    
    logger.info("Exit admin`s /start handler")
    
# command /test 'only' for admin
@admin_router.message(
    Command(commands="stats"),
    flags={"long_operation": "typing"}
)
async def cmd_test(message: Message):
    await asyncio.sleep(3)
    await message.answer('Here is statistics, admin!')
