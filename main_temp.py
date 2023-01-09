from aiogram import Bot, Dispatcher, executor, types
import config

bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

HELP_COMMAND = '''
<b>/start</b> - <em>Run the Bot!</em>
<b>/help</b> - <em>Got help?</em>
'''


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['photo'])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://qph.cf2.quoracdn.net/main-qimg-1947fbba660f801fbb2261c4e6d7a336-lq')


@dp.message_handler(commands='location')
async def send_coord(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id,
                            latitude=55,
                            longitude=50)
    await message.delete()


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Hello')


if __name__ == '__main__':
    executor.start_polling(dp)
