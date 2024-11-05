import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.keyboards import url_keyboard, create_records_keyboard

logger = logging.getLogger(__name__)

# creating router`s onject
user_router = Router(name='user router')


# command /start for everyone
# @user_router.message(CommandStart())
# async def cmd_user_start(message: Message):
#     logger.info("Enter user`s /start handler")
    
#     await message.answer('You sent /start, user')
    
#     logger.debug("Exit user`s /start handler")


# command /weight 'only' for user
@user_router.message(Command(commands='weight'))
async def cmd_weight(message: Message):
    await message.answer('Your weight record was add to database, user!')
    
    
# command /measure 'only' for user
@user_router.message(Command(commands="measure"))
async def cmd_measure(message: Message):
    await message.answer("Your measure record was add to database, user!")


# command for /diet for everyone
@user_router.message(Command(commands='diet'))
async def cmd_diet(message: Message):
    await message.answer(
        text='Here are your food and goal',
        reply_markup=url_keyboard
    )


# commands for /record for everyone
@user_router.message(Command(commands='record'))
async def cmd_record(message: Message):
    await message.answer(
        text='What do you want to write down?',
        reply_markup=create_records_keyboard()
    )
