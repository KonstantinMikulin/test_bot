from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
import hashlib

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

user_data = ''


async def on_startup(_):
    print('Bot is running')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text='Input your number')


@dp.message_handler()
async def text_handler(message: types.Message):
    global user_data
    user_data = message.text

    if message.text.isdigit():
        await message.reply(text='Your data was saved')


@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery):
    text = inline_query.query or 'Echo'
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    input_content = InputTextMessageContent(f'<b>{text}</b> - {user_data}',
                                            parse_mode='html')

    item = InlineQueryResultArticle(input_message_content=input_content,
                                    id=result_id,
                                    title='Echo Bot!',
                                    description='Hello I`m The Bot!')

    await bot.answer_inline_query(results=[item],
                                  inline_query_id=inline_query.id,
                                  cache_time=1)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
