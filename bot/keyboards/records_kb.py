from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kg_button = InlineKeyboardButton(
    text='Weight',
    callback_data='weight_btn_pressed'
)

cm_button = InlineKeyboardButton(
    text='Measure',
    callback_data='measure_btn_pressed'
)

records_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[kg_button], [cm_button]]
)
