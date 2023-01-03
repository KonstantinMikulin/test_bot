from aiogram import Bot, Dispatcher, executor, types
import config


bot = Bot(config.TOKEN)
dp = Dispatcher(bot)


HELP_COMMAND = '''
<b>/start</b> - Run the Bot!
<b>/help</b> - Got help?
'''


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND, parse_mode='HTML')


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='Hello')


if __name__ == '__main__':
    executor.start_polling(dp)
