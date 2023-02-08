from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent
from aiogram.utils.callback_data import CallbackData
import hashlib

from config import TOKEN

cb = CallbackData('ikb', 'action')
bot = Bot(TOKEN)
dp = Dispatcher(bot)


def get_ikb():
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Button 1', callback_data=cb.new('push 1'))],
        [InlineKeyboardButton(text='Button 2', callback_data=cb.new('push 2'))]
    ])

    return ikb


async def on_startup(_):
    print('Bot is running')


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer(text='Welcome to The Bot',
                         reply_markup=get_ikb())


@dp.callback_query_handler(cb.filter(action='push 1'))
async def push1_cb_hand(callback: types.CallbackQuery):
    await callback.answer(text='Hello!')


@dp.callback_query_handler(cb.filter(action='push 2'))
async def push2_cb_hand(callback: types.CallbackQuery):
    await callback.answer(text='World!')


@dp.inline_handler() # process InlineQuery() is formed by Telegram API
async def inline_echo(inline_query: types.InlineQuery):
    text = inline_query.query or 'Echo'  # получили текст от пользователя
    input_content = InputTextMessageContent(text)  # формируем контент ответного сообщения
    result_id = hashlib.md5(text.encode()).hexdigest()  # сделали уникальный ID результата
    item = InlineQueryResultArticle(
        input_message_content=input_content,
        id=result_id,
        title='Echo!!!'
    )

    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item],
                                  cache_time=1)



if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
