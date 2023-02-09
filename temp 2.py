from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
import uuid

from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot is running')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text='Hello! I`m the Bot')


@dp.inline_handler()
async def inline_article(inline_query: types.InlineQuery):
    text = inline_query.query or 'Empty'
    input_content_bold = InputTextMessageContent(message_text=f'*{text}*',
                                                 parse_mode='markdown')
    input_content_italic = InputTextMessageContent(message_text=f'_{text}_',
                                                   parse_mode='markdown')

    item_1 = InlineQueryResultArticle(id=str(uuid.uuid4()),
                                      input_message_content=input_content_bold,
                                      title='Bold',
                                      description=text,
                                      thumb_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTu8S4D8vnu9XgYneqlE0MF-y1bM53aCuwTxQ&usqp=CAU'
                                      )

    item_2 = InlineQueryResultArticle(id=str(uuid.uuid4()),
                                      input_message_content=input_content_italic,
                                      title='Italic',
                                      description=text,
                                      thumb_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVkcF3NDbExq1RrPssgteKcAY1R8xY_KZPvg&usqp=CAU'
                                      )

    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item_1, item_2],
                                  cache_time=1)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           skip_updates=True)
