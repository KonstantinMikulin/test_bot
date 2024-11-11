import asyncio
import logging

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio.engine import AsyncEngine

logger = logging.getLogger(__name__)

# creating router`s onject
admin_router = Router(name="admin router")


# /start command add data about user into db
@admin_router.message(CommandStart())
async def cmd_admin_start(message: Message, state:FSMContext):
    logger.info("Enter admin`s /start handler")
    
    await state.clear()
    
    await message.answer('<b>Admin</b>, you sent /start! Welcome!')
    
    logger.info("Exit admin`s /start handler")
    

#TODO: make it works
@admin_router.message(Command(commands="deleteme"))
async def cmd_delteme(message: Message, db_engine: AsyncEngine):
    await message.answer("Your data was delete")


# TODO: make it works
# command /test 'only' for admin
@admin_router.message(
    Command(commands="stats"),
    flags={"long_operation": "typing"}
)
async def cmd_test(message: Message):
    await asyncio.sleep(3)
    await message.answer('Here is statistics, admin!')
