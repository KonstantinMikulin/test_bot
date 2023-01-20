from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randrange
import string
import config

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

HELP_COMMAND = '''
<b>/start</b> <em>- Run tha Bot!</em>
<b>/help</b> <em>- show some help</em>
<b>/give</b> <em>- Give me some</em>
'''

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


async def on_startup_msg(_):
    print('Bot is running')


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Welcome',
                           reply_markup=keyboard)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer('This bot can do not so much')
    await message.delete()


@dp.message_handler(commands=['give'])
async def send_sticker(message: types.Message):
    await message.answer('What is it? 👇🏻')
    await bot.send_sticker(message.from_user.id,
                           sticker='CAACAgUAAxkBAAEHHGBjtEA8BvZS2jNkA-jZn8jXxCAijQAChQMAAukKyANnDaiEsg4V0S0E')


@dp.message_handler(commands=['photo'])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://qph.cf2.quoracdn.net/main-qimg-1947fbba660f801fbb2261c4e6d7a336-lq')
    await message.delete()


@dp.message_handler(commands='location')
async def send_coord(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id,
                            latitude=55,
                            longitude=50)
    await message.delete()


@dp.message_handler(commands=['❤️'])
async def black_heart(message: types.Message):
    await message.answer('🖤')


@dp.message_handler()
async def check_zero(message: types.Message):
    if '0' in message.text:
        await message.answer('OFF')
    elif '1' in message.text:
        await message.answer('ON')
    else:
        await message.answer(message.text)


@dp.message_handler(content_types=['sticker'])
async def get_id(message: types.Message):
    await message.answer(message.sticker.file_id)


@dp.message_handler(commands='links')
async def links_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Here you are',
                           reply_markup=inline_keyboard)
    await message.delete()


# @dp.message_handler(commands='location')
# async def send_random_location(message: types.Message):
#     await bot.send_location(chat_id=message.chat.id,
#                             latitude=randrange(1, 90),
#                             longitude=randrange(1, 90))



# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(text=message.text)


# @dp.message_handler()
# async def echo2(message: types.Message):
#     if 'Hello' in message.text:
#         await message.answer(text='Привет, привет!')
#     else:
#         await message.reply(text='А здороваться?')


# @dp.message_handler()
# async def echo3(message: types.Message):
#     if 'Hello' in message.text:
#         await message.answer(text=message.text)


# @dp.message_handler()
# async def send_random_letter(message: types.Message):
#     await message.reply(random.choice(string.ascii_letters))


# @dp.message_handler()
# async def echo4(message: types.Message):
#     if message.text.count(' ') == 1:
#         await message.answer(text=message.text)


# @dp.message_handler()
# async def count_chars(message: types.Message):
#     await message.reply(str(message.text.count('❤️')))


# @dp.message_handler()
# async def have_a_heart(message: types.Message):
#     if '❤️' in message.text or message.text == '❤️':
#         await message.reply('🖤')
#     else:
#         await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup_msg, skip_updates=True)
