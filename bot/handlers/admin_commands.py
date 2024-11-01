from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from bot.filters import IsAdminFilter

# creating router`s onject
admin_router = Router(name="admin router")


@admin_router.message(CommandStart(), IsAdminFilter())
async def cmd_admin_start(message: Message):
    await message.answer('Admin, you sent /start! Welcome!')


# command /test 'only' for admin
@admin_router.message(Command(commands='stats'))
async def cmd_test(message: Message):
    await message.answer('Here is statistics, admin!')
