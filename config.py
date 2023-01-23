from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


TOKEN ='5751024125:AAFHkyBrgab3LVI_OpmmpHoyhw-ts2Dqlo4'


keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=True)
button1 = KeyboardButton('/help')
button2 = KeyboardButton('/vote')
keyboard.add(button1, button2)

inline_keyboard = InlineKeyboardMarkup(row_width=2)
inline_button1 = InlineKeyboardButton(text='👍',
                                      callback_data='like')
inline_button2 = InlineKeyboardButton(text='👎🏻',
                                      callback_data='dislike')
# inline_button3 = InlineKeyboardButton(text='link 3',
#                                       url='https://vk.com/')
# inline_button4 = InlineKeyboardButton(text='link 4',
#                                       url='https://github.com/')
#inline_keyboard.add(inline_button1, inline_button2, inline_button3, inline_button4)
inline_keyboard.add(inline_button1, inline_button2)