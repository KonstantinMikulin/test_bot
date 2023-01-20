from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

button1 = InlineKeyboardButton('start')
button2 = InlineKeyboardButton('help')


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           reply_markup=InlineKeyboardMarkup)


if __name__ == '__main__':
    executor.start_polling(dp)