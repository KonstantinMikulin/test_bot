from aiogram import Bot, Dispatcher, executor, types
from random import randrange, choice

import config

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot is running')


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Welcome')
    await message.delete()


@dp.message_handler(commands='help')
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=config.help_commands,
                           parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands='description')
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='This bot can do not so much :(')
    await message.delete()


@dp.message_handler(commands='keyboard')
async def keyboard_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Here you go',
                           reply_markup=config.keyboard1)
    await message.delete()


@dp.message_handler(commands='emoji')
async def emoji_command(message: types.Message):
    await message.answer('🤟🏻')
    await message.delete()


@dp.message_handler(commands='sticker')
async def sticker_command(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker='CAACAgUAAxkBAAEHZsFjzsDqPa36ZPlODbcIr7pTyW6RdgACsQEAAqqYQFfPcvuENG4vGy0E')
    await message.delete()


@dp.message_handler(commands='location')
async def location_command(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=randrange(1, 50),
                            longitude=randrange(1, 50))
    await message.delete()


@dp.message_handler(commands='photo')
async def photo_command(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         caption='Like it or not?!',
                         photo=choice(config.list_of_photos),
                         reply_markup=config.inline_keyboard)
    await message.delete()


@dp.message_handler(commands='vote')
async def vote_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Let`s play!',
                           reply_markup=config.keyboard2)
    await message.delete()


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text='You like it!')
    elif callback.data == 'dislike':
        await callback.answer(text='You don`t like it!')
    else:
        await callback.answer(text='Ok')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)

# TODO: инлайн клавиатура должна состоять из трёх кнопок: 1. Следующее фото. 2. Лайк 3. Дизлайк. Сделать обработку повторного нажатия на одну и ту же фотографию.
