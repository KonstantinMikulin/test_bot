from aiogram import Bot, Dispatcher, executor, types
import config

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

HELP_COMMANDS = '''
/help или /помощь - список команд
/start или /старт - начало работы
'''


@dp.message_handler(commands=['start', 'старт'])
async def start_command(message: types.Message):
    await message.answer(text='Welcome')
    await message.delete()


@dp.message_handler(commands=['help', 'помощь'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMANDS)
    await message.delete()


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
