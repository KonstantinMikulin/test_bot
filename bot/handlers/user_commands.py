from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from bot.keyboards import url_keyboard

# creating router`s onject
router = Router(name='user router')


# command /start for everyone
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello user or admin!')


# command /check 'only' for user
@router.message(Command(commands='weight'))
async def cmd_check(message: Message):
    await message.answer('Your record was add to database, user!')


# command for /diet for everyone
@router.message(Command(commands='diet'))
async def cmd_diet(message: Message):
    await message.answer(
        text='Heare your food and goal',
        reply_markup=url_keyboard
    )
