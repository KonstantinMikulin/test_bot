from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from bot.filters.main_filters import IsAdminFilter

# creating router`s onject
router = Router(name="admin router")


@router.message(CommandStart(), IsAdminFilter())
async def cmd_admin_start(message: Message):
    await message.answer('Admin, you sent /start! Welcome!')


# command /test 'only' for admin
@router.message(Command(commands='stats'))
async def cmd_test(message: Message):
    await message.answer('Here is statistics, admin!')
