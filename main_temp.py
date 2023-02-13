from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.middlewares import BaseMiddleware

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


class TestMiddleWare(BaseMiddleware):

    async def on_process_update(self, update, data):
        print('Process update done')

    async def on_pre_process_update(self, update: types.Update, data: dict):
        print('Hello!')


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer(text='Started')
    print('World!')


if __name__ == '__main__':
    dp.middleware.setup(TestMiddleWare())
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)
