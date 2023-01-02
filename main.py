from aiogram import Bot, Dispatcher, executor, types
import string
import config

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

HELP_COMMAND = '''
/help - список команд
/start - начало работы
'''


@dp.message_handler(commands=['start', 'старт'])
async def help_command(message: types.Message):
    await message.answer(text='Welcome')
    await message.delete()


@dp.message_handler(commands=['help', 'помощь'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer('This bot can do not so much')
    await message.delete()


# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(text=message.text)


@dp.message_handler()
async def echo(message: types.Message):
    if 'Hello' in message.text:
        await message.answer(text='Привет, привет!')
    else:
        await message.reply(text='А здороваться?')


# @dp.message_handler()
# async def echo(message: types.Message):
#     if 'Hello' in message.text:
#         await message.answer(text=message.text)


# @dp.message_handler()
# async def send_random_letter(message: types.Message):
#     await message.reply(random.choice(string.ascii_letters))


# @dp.message_handler()
# async def echo(message: types.Message):
#     if message.text.count(' ') == 1:
#         await message.answer(text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
