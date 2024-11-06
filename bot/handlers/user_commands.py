import logging
from random import randint

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from sqlalchemy.ext.asyncio import AsyncSession

from bot.keyboards import url_keyboard, create_records_keyboard
from bot.db import add_weight

logger = logging.getLogger(__name__)

# creating router`s onject
user_router = Router(name='user router')


# command /weight 'only' for user
@user_router.message(Command(commands='weight'))
async def cmd_weight(message: Message, session: AsyncSession):
    weight = randint(70, 100)
    
    await add_weight(
        session=session,
        telegram_id=message.from_user.id, # type:ignore
        weight=weight
    )
    await message.answer(f'Your weight: {weight} kg added to database, user!')
    

#TODO: make it works
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
