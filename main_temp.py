from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.middlewares import BaseMiddleware

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


class CustomMiddleware(BaseMiddleware):

    async def on_pre_process_update(self, update: types.Update, data: dict):
        pass

    async def on_process_update(self, update: types.Update, data: dict):
        pass

    async def on_process_message(self, message: types.Message, data: dict):
        print(data, message)


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton('Test', callback_data='data')]
    ])
    await message.answer(text='Started',
                         reply_markup=ikb)


if __name__ == '__main__':
    dp.middleware.setup(CustomMiddleware())
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)
