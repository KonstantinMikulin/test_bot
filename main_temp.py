from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

cb = CallbackData('ikb', 'action')

ikb = InlineKeyboardMarkup(inline_keyboard=[
                           [InlineKeyboardButton('Button', callback_data=cb.new('push'))]
                           ])


async def on_startup(_):
    print('Bot is running')


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer(text='One two three',
                         reply_markup=ikb)


@dp.callback_query_handler(cb.filter())
async def ikb_cb_handler(callback: types.CallbackQuery, callback_data: dict):
    if callback_data['action'] == 'push':
        await callback.answer(text='Something')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
