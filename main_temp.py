from aiogram import Bot, Dispatcher, executor, types
import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

HELP_COMMANDS = '''
<b>/help</b> <em>- show some help!</em>
'''
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text=HELP_COMMANDS,
                           parse_mode='HTML')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
