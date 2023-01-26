from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# bot`s token
TOKEN ='5751024125:AAFHkyBrgab3LVI_OpmmpHoyhw-ts2Dqlo4'

# reply keyboards
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True,
                                one_time_keyboard=True)
button1 = KeyboardButton(text='/help')
button2 = KeyboardButton(text='/description')
button3 = KeyboardButton(text='/emoji')
button4 = KeyboardButton(text='/sticker')
button5 = KeyboardButton(text='/location')
button6 = KeyboardButton(text='/photo')
button7 = KeyboardButton(text='/vote')
keyboard1.add(button1, button2).add(button3, button4).add(button5, button6).add(button7)

keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True,
                                one_time_keyboard=True)
button2_1 = KeyboardButton(text='/photo')
button2_2 = KeyboardButton(text='/keyboard')
keyboard2.add(button2_1, button2_2)

# inline keyboard
inline_keyboard = InlineKeyboardMarkup(row_width=2)
inline_button1 = InlineKeyboardButton(text='👍🏻',
                                      callback_data='like')
inline_button2 = InlineKeyboardButton(text='👎🏻',
                                      callback_data='dislike')
inline_button3 = InlineKeyboardButton(text='Next',
                                      callback_data='next')
inline_keyboard.add(inline_button1, inline_button2, inline_button3)


# list of command for /help
help_commands = '''
<b>LIST OF COMMANDS</b>

<b>start</b> - run the bot!
<b>help</b> - list of commands
<b>description</b> - main idea
<b>keyboard</b> - run keyboard
<b>emoji</b> - send some emoji
<b>sticker</b> - send some sticker
<b>location</b> - send random location
<b>photo</b> - send random photo
'''

# list and description of photos for random choice
list_of_photos = ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTdEch9IuKWFMWoxycfGiGhRc9SOCOb7axEg&usqp=CAU',
                  'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaypMM-0kZeSBkzZJi_XNlsOICyfwI4UAR6Q&usqp=CAU',
                  'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpNGN2F7NQGrxO3uTs4r0yF8yuCUq4kBwqAw&usqp=CAU',
                  'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMzmn84CZqMM3f1jK009KsRRf_W8q5vF0q-g&usqp=CAU',
                  'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQynvRxKmTmU4hINNOFvwkpDIcVuM-7wMn8Ag&usqp=CAU']

descriptions_photos = ['Chuck',
                       'Bruce',
                       'Arnold',
                       'Sylvester',
                       'Sean']

photos = dict(zip(list_of_photos, descriptions_photos))


# keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
#                                one_time_keyboard=True)
# button1 = KeyboardButton('/help')
# button2 = KeyboardButton('/vote')
# keyboard.add(button1, button2)
#
# inline_keyboard = InlineKeyboardMarkup(row_width=2)
# inline_button1 = InlineKeyboardButton(text='👍',
#                                       callback_data='like')
# inline_button2 = InlineKeyboardButton(text='👎🏻',
#                                       callback_data='dislike')
# # inline_button3 = InlineKeyboardButton(text='link 3',
# #                                       url='https://vk.com/')
# # inline_button4 = InlineKeyboardButton(text='link 4',
# #                                       url='https://github.com/')
# #inline_keyboard.add(inline_button1, inline_button2, inline_button3, inline_button4)
# inline_keyboard.add(inline_button1, inline_button2)