from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

# creating router`s onject
router = Router(name="admin router")


# command /test 'only' for admin
@router.message(Command(commands='stats'))
async def cmd_test(message: Message):
    await message.answer('Here is statistics, admin!')
