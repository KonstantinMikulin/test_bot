from aiogram import Bot, Dispatcher, executor,types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

import config

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot is running')


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Welcome',
                           reply_markup=config.keyboard)


@dp.message_handler(commands='vote')
async def vote_command(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker='CAACAgUAAxkBAAEHZsFjzsDqPa36ZPlODbcIr7pTyW6RdgACsQEAAqqYQFfPcvuENG4vGy0E')
    await bot.send_message(chat_id=message.chat.id,
                           text='Vote, please',
                           reply_markup=config.inline_keyboard)


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text='You like it!')
    else:
        await callback.answer(text='You don`t like it')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
