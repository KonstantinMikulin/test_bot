from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import config

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=True)

button1 = KeyboardButton('/help')
button2 = KeyboardButton('/description')
button3 = KeyboardButton('❤️')

keyboard.add(button1).add(button2).add(button3)

HELP_COMMANDS = '''
<b>/start</b> - Run The Bot!
<b>/help</b> - Need some?
<b>/description</b> - This is The Bot
'''


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await message.answer('Welcome!',
                         reply_markup=keyboard)


@dp.message_handler(commands='help')
async def help_command(message: types.Message):
    await bot.send_message(message.chat.id,
                           text=HELP_COMMANDS,
                           parse_mode='HTML')


@dp.message_handler(commands='description')
async def description_command(message: types.Message):
    await bot.send_message(message.chat.id,
                           text='This is The Bot')


@dp.message_handler(commands='❤️')
async def send_heart_command(message: types.Message):
    await bot.send_message(message.chat.id,
                           text='❤️')


@dp.message_handler(commands='sendlove')
async def send_love_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Ань, ну ты чо?! :)')


@dp.message_handler(commands='sticker')
async def send_sticker_command(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker='CAACAgUAAxkBAAEHHGBjtEA8BvZS2jNkA-jZn8jXxCAijQAChQMAAukKyANnDaiEsg4V0S0E')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
