from aiogram import Bot, Dispatcher, executor, types
import config


bot = Bot(config.TOKEN)
dp = Dispatcher(bot)


# @dp.message_handler()
# async def echo (message: types.Message):
#     await message.answer(text=message.text.upper())

@dp.message_handler()
async def echo (message: types.Message):
    if message.text.count(' ') == 1:
        await message.answer(text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
