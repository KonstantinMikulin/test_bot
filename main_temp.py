from aiogram import Bot, Dispatcher, executor, types
from random import randrange

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
                           reply_markup=config.keyboard)
    await message.delete()


# TODO: добавить функцию отправки эмодзи, стикера и рандомного местоположения

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
    await bot.send_location(chat_id=message.chat.id,)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)


# TODO: клавиатура с командой получение одной рандомной фотографии из заранее определённого списка. Из этого меня должен быть переход в основное меню

# TODO: должно быть описание к этому фото и инлайн клавиатура к нему

# TODO: клавиатура должна генерировать callback запрос и обработка запроса со стороны сервера

# TODO: инлайн клавиатура должна состоять из трёх кнопок: 1. Следующее фото. 2. Лайлю 3. Дизлайк. Сделать обработку повторного нажатия на одну и ту же фотографию.


