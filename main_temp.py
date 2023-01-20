from aiogram import Bot, Dispatcher, executor, types

import config

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot is running!')


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Welcome',
                           reply_markup=config.keyboard)
    await message.delete()


@dp.message_handler(commands='links')
async def links_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Here you are',
                           reply_markup=config.inline_keyboard)
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
