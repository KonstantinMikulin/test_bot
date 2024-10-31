from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

url_btn_1 = InlineKeyboardButton(
    text="Food",
    url="https://ru.wikipedia.org/wiki/%D0%9A%D0%BD%D0%B8%D0%B3%D0%B0_%D0%BE_%D0%B2%D0%BA%D1%83%D1%81%D0%BD%D0%BE%D0%B9_%D0%B8_%D0%B7%D0%B4%D0%BE%D1%80%D0%BE%D0%B2%D0%BE%D0%B9_%D0%BF%D0%B8%D1%89%D0%B5",
)

url_btn_2 = InlineKeyboardButton(
    text="Goal",
    url="https://ru.wikipedia.org/wiki/%D0%93%D0%B0%D1%80%D0%B3%D0%B0%D0%BD%D1%82%D1%8E%D0%B0_%D0%B8_%D0%9F%D0%B0%D0%BD%D1%82%D0%B0%D0%B3%D1%80%D1%8E%D1%8D%D0%BB%D1%8C",
)

url_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[url_btn_1], [url_btn_2]]
)
