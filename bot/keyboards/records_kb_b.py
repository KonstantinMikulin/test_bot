from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

records_commands = {
    "Weight": "weight_btn_pressed",
    "Measure": "measure_btn_pressed"
}


# function for creating keyboard with type of records
def create_records_keyboard():
    kb_builder = InlineKeyboardBuilder()
    
    buttons: list[InlineKeyboardButton] = [] #type:ignore
    
    for button in records_commands:
        buttons.append(InlineKeyboardButton(
            text=button,
            callback_data=records_commands.get(button)
        ))

    kb_builder.row(*buttons, width=2)
    
    return kb_builder.as_markup()
