from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot is running!')


keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=True)
button1 = KeyboardButton('/start')
button2 = KeyboardButton('/links')
keyboard.add(button1, button2)

inline_keyboard = InlineKeyboardMarkup(row_width=3)
inline_button1 = InlineKeyboardButton(text='link 1',
                                      url='https://ru.wikipedia.org/')
inline_button2 = InlineKeyboardButton(text='link 2',
                                      url='https://www.youtube.com/')
inline_button3 = InlineKeyboardButton(text='link 3',
                                      url='https://vk.com/')
inline_button4 = InlineKeyboardButton(text='link 4',
                                      url='https://github.com/')
inline_keyboard.add(inline_button1, inline_button2, inline_button3, inline_button4)


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Welcome',
                           reply_markup=keyboard)
    await message.delete()


@dp.message_handler(commands='links')
async def links_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Here you are',
                           reply_markup=inline_keyboard)
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
