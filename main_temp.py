from aiogram import Bot, Dispatcher,executor, types
from config import TOKEN, inline_keyboard

bot = Bot(TOKEN)
dp = Dispatcher(bot)
number = 0


async def on_startup(_):
    print('Bot is running')


def get_inline_keyboard():
    return inline_keyboard  # keyboard from config file


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    global number

    await message.answer(text=f'Current number is {number}',
                         reply_markup=get_inline_keyboard())


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('btn'))
async def cb_counter(callback: types.CallbackQuery):
    global number

    if callback.data == 'btn_increase':
        number += 1
        await callback.message.edit_text(f'Current number is {number}',
                                         reply_markup=get_inline_keyboard())
    else:
        number -= 1
        await callback.message.edit_text(f'Current number is {number}',
                                         reply_markup=get_inline_keyboard())


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
