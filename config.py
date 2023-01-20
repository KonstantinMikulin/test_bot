from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


TOKEN ='5751024125:AAFHkyBrgab3LVI_OpmmpHoyhw-ts2Dqlo4'


keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=True)
button1 = KeyboardButton('/start')
button2 = KeyboardButton('/links')
keyboard.add(button1, button2)

inline_keyboard = InlineKeyboardMarkup(row_width=3)
inline_button1 = InlineKeyboardButton(text='link 1',
                                      url='https://ru.wikipedia.org/')
inline_button2 = InlineKeyboardButton(text='link 2',
                                      url='https://www.youtube.com/')
inline_button3 = InlineKeyboardButton(text='link 3',
                                      url='https://vk.com/')
inline_button4 = InlineKeyboardButton(text='link 4',
                                      url='https://github.com/')
inline_keyboard.add(inline_button1, inline_button2, inline_button3, inline_button4)