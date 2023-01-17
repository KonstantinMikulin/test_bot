from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import config

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=True)

button1 = KeyboardButton('/help')
button2 = KeyboardButton('/description')

keyboard.add(button1).add(button2)

HELP_COMMANDS = '''
<b>/start</b> - Run The Bot!
<b>/help</b> - Need some?
<b>/description</b> - This is The Bot
'''


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text='Welcome!',
                           reply_markup=keyboard)


@dp.message_handler(commands='help')
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text=HELP_COMMANDS,
                           parse_mode='HTML')


@dp.message_handler(commands='description')
async def description_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text='This is The Bot')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
