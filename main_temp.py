from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from random import randrange, choice

import config

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

random_photo = choice(list(config.photos.keys()))
flag_like = False
flag_dislike = False


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
    random_photo = choice(list(config.photos.keys()))
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random_photo,
                         caption=config.photos[random_photo],
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
    global random_photo
    global flag_like
    global flag_dislike
    if callback.data == 'like':
        if not flag_like:
            await callback.answer(text='You like it!')
            flag_like = not flag_like
        else:
            await callback.answer(text='You liked it already')
    elif callback.data == 'dislike':
        if not flag_dislike:
            await callback.answer(text='You don`t like it!')
            flag_dislike = not flag_dislike
        else:
            await callback.answer(text='You don`t like it already!')
    else:
        random_photo = choice(list(filter(lambda x: x != random_photo, list(config.photos.keys()))))
        await callback.message.edit_media(types.InputMedia(media=random_photo,
                                                           type='photo',
                                                           caption=config.photos[random_photo]),
                                          reply_markup=config.inline_keyboard)
        await callback.answer()


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
