from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler, current_handler

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


def set_key(key: str = None):
    def decorator(func):
        setattr(func, 'key', key)

        return func

    return decorator


class AdminMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        handler = current_handler.get()

        if handler:
            key = getattr(handler, 'key', 'Такого атрибута нет')
            print(key)


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.reply(text='Started')


@dp.message_handler(lambda message: message.text.lower() == 'hello')
@set_key('hello')
async def text_hello(message: types.Message):
    await message.reply('Hello you!')


if __name__ == '__main__':
    dp.middleware.set(AdminMiddleware)
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)
