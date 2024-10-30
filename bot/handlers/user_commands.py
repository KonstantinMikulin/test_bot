from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

# creating router`s onject
router = Router(name='user router')


# command /start for everyone
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello user or admin!')


# command /check 'only' for user
@router.message(Command(commands='check'))
async def cmd_check(message: Message):
    await message.answer('Hello, user!')
