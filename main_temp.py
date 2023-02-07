from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

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


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
