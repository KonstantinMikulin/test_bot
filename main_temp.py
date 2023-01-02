from aiogram import Bot, Dispatcher, executor, types
import config
import string
import random

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer('This bot can do not so much')
    await message.delete()


@dp.message_handler()
async def send_random_letter(message: types.Message):
    await message.reply(random.choice(string.ascii_letters))


if __name__ == '__main__':
    executor.start_polling(dp)
