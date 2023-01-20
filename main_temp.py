from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

inline_keyboard = InlineKeyboardMarkup(row_width=2)
inline_button1 = InlineKeyboardButton(text='WiKi',
                                  url='https://ru.wikipedia.org/')
inline_button2 = InlineKeyboardButton(text='YouTube',
                                  url='https://www.youtube.com/')

inline_keyboard.add(inline_button1, inline_button2)




@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Welcome!',
                           reply_markup=inline_keyboard)


@dp.message_handler(commands='help')
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Need help?')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)