from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
from aiogram.utils.callback_data import CallbackData
from random import randrange
from aiogram.utils.exceptions import BotBlocked
import string
import hashlib

import config
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)


# шаблон CallbackData

#cb = CallbackData('ikb', 'action')

# ikb = InlineKeyboardMarkup(inline_keyboard=[
#                            [InlineKeyboardButton('Button', callback_data=cb.new('push'))]
#                            ])

HELP_COMMAND = '''
<b>/start</b> <em>- Run tha Bot!</em>
<b>/help</b> <em>- show some help</em>
<b>/give</b> <em>- Give me some</em>
'''


async def on_startup_msg(_):
    print('Bot is running')


def get_inline_keyboard():
    return inline_keyboard  # keyboard from config file


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Welcome',
                           reply_markup=config.keyboard1)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer('This bot can do not so much')
    await message.delete()


@dp.message_handler(commands=['give'])
async def send_sticker(message: types.Message):
    await message.answer('What is it? 👇🏻')
    await bot.send_sticker(message.from_user.id,
                           sticker='CAACAgUAAxkBAAEHHGBjtEA8BvZS2jNkA-jZn8jXxCAijQAChQMAAukKyANnDaiEsg4V0S0E')


@dp.message_handler(commands=['photo'])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://qph.cf2.quoracdn.net/main-qimg-1947fbba660f801fbb2261c4e6d7a336-lq')
    await message.delete()


@dp.message_handler(commands='location')
async def send_coord(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id,
                            latitude=55,
                            longitude=50)
    await message.delete()


@dp.message_handler(commands=['❤️'])
async def black_heart(message: types.Message):
    await message.answer('🖤')


@dp.message_handler()
async def check_zero(message: types.Message):
    if '0' in message.text:
        await message.answer('OFF')
    elif '1' in message.text:
        await message.answer('ON')
    else:
        await message.answer(message.text)


@dp.message_handler(content_types=['sticker'])
async def get_id(message: types.Message):
    await message.answer(message.sticker.file_id)


@dp.message_handler(commands='links')
async def links_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Here you are',
                           reply_markup=config.inline_keyboard)
    await message.delete()


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


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    print('Нельзя отправить сообщение, потому что бот заблокирован')

    return True


# def get_ikb():
#     ikb = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text='Button 1', callback_data=cb.new('push 1'))],
#         [InlineKeyboardButton(text='Button 2', callback_data=cb.new('push 2'))]
#     ])
#
#     return ikb


# @dp.callback_query_handler(cb.filter())
# async def ikb_cb_handler(callback: types.CallbackQuery, callback_data: dict):
#     if callback_data['action'] == 'push':
#         await callback.answer(text='Something')


# @dp.callback_query_handler(cb.filter(action='push 1'))
# async def push1_cb_hand(callback: types.CallbackQuery):
#     await callback.answer(text='Hello!')
#
#
# @dp.callback_query_handler(cb.filter(action='push 2'))
# async def push2_cb_hand(callback: types.CallbackQuery):
#     await callback.answer(text='World!')


# @dp.inline_handler() # process InlineQuery() is formed by Telegram API
# async def inline_echo(inline_query: types.InlineQuery):
#     text = inline_query.query or 'Echo'  # получили текст от пользователя
#     input_content = InputTextMessageContent(text)  # формируем контент ответного сообщения
#     result_id = hashlib.md5(text.encode()).hexdigest()  # сделали уникальный ID результата
#
#     if text == 'photo':
#         input_content = InputTextMessageContent('This is photo')
#
#     item = InlineQueryResultArticle(
#         input_message_content=input_content,
#         id=result_id,
#         title=text
#     )
#
#     await bot.answer_inline_query(inline_query_id=inline_query.id,
#                                   results=[item])



# @dp.message_handler(commands='location')
# async def send_random_location(message: types.Message):
#     await bot.send_location(chat_id=message.chat.id,
#                             latitude=randrange(1, 90),
#                             longitude=randrange(1, 90))



# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(text=message.text)


# @dp.message_handler()
# async def echo2(message: types.Message):
#     if 'Hello' in message.text:
#         await message.answer(text='Привет, привет!')
#     else:
#         await message.reply(text='А здороваться?')


# @dp.message_handler()
# async def echo3(message: types.Message):
#     if 'Hello' in message.text:
#         await message.answer(text=message.text)


# @dp.message_handler()
# async def send_random_letter(message: types.Message):
#     await message.reply(random.choice(string.ascii_letters))


# @dp.message_handler()
# async def echo4(message: types.Message):
#     if message.text.count(' ') == 1:
#         await message.answer(text=message.text)


# @dp.message_handler()
# async def count_chars(message: types.Message):
#     await message.reply(str(message.text.count('❤️')))


# @dp.message_handler()
# async def have_a_heart(message: types.Message):
#     if '❤️' in message.text or message.text == '❤️':
#         await message.reply('🖤')
#     else:
#         await message.reply(message.text)


# @dp.callback_query_handler(text='remove all')
# async def remove_cb_data(callback: types.CallbackQuery):
#     await callback.message.delete()
#
#
# @dp.callback_query_handler()
# async def photo_callback(callback:  types.CallbackQuery):
#     global is_voted
#
#     if not is_voted:
#         if callback.data == 'like':
#             await callback.answer(text='You like it!')
#             is_voted = True
#         await callback.answer(text='You dont like it :(')
#         is_voted = True
#     await callback.answer(text='You voted ALREDY!',
#                           show_alert=True)
#
#
#     if callback.data == 'like':
#         if not is_voted:
#             await callback.answer(text='You like it!')
#             is_voted = not is_voted
#         else:
#             await callback.answer(text='You voted already!')
#     elif callback.data == 'dislike':
#         if not is_voted:
#             await callback.answer(text='You dont like it :(')
#             is_voted = not is_voted
#         else:
#             await callback.answer(text='You voted ALREADY!')


# @dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('btn'))
# async def cb_counter(callback: types.CallbackQuery):
#     global number
#
#     if callback.data == 'btn_increase':
#         number += 1
#         await callback.message.edit_text(f'Current number is {number}',
#                                          reply_markup=get_inline_keyboard())
#     elif callback.data == 'btn_decrease':
#         number -= 1
#         await callback.message.edit_text(f'Current number is {number}',
#                                          reply_markup=get_inline_keyboard())
#     else:
#         number = randint(0, 1000)
#         await callback.message.edit_text(f'Current number is {number}',
#                                          reply_markup=get_inline_keyboard()))


# два всплюывающих окна для работы в инлайн режиме
# @dp.inline_handler()
# async def inline_article(inline_query: types.InlineQuery):
#     text = inline_query.query or 'Empty'
#     input_content_bold = InputTextMessageContent(message_text=f'*{text}*',
#                                                  parse_mode='markdown')
#     input_content_italic = InputTextMessageContent(message_text=f'_{text}_',
#                                                    parse_mode='markdown')
#
#     item_1 = InlineQueryResultArticle(id=str(uuid.uuid4()),
#                                       input_message_content=input_content_bold,
#                                       title='Bold',
#                                       description=text,
#                                       thumb_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTu8S4D8vnu9XgYneqlE0MF-y1bM53aCuwTxQ&usqp=CAU'
#                                       )
#
#     item_2 = InlineQueryResultArticle(id=str(uuid.uuid4()),
#                                       input_message_content=input_content_italic,
#                                       title='Italic',
#                                       description=text,
#                                       thumb_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVkcF3NDbExq1RrPssgteKcAY1R8xY_KZPvg&usqp=CAU'
#                                       )
#
#     await bot.answer_inline_query(inline_query_id=inline_query.id,
#                                   results=[item_1, item_2],
#                                   cache_time=1)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup_msg, skip_updates=True)
