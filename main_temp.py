from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

HELP_COMMANDS = '''
<b>/help</b> <em>- show some help!</em>
'''

keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=True)
button1 = KeyboardButton('/help')
button2 = KeyboardButton('/start')
button3 = KeyboardButton('/description')
keyboard.add(button1).add(button2).add(button3)


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text='Welcome',
                           reply_markup=keyboard)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text=HELP_COMMANDS,
                           parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text='This bot can do not so much')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
