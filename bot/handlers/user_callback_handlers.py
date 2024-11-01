from aiogram import Router, F
from aiogram.types import CallbackQuery

user_callback_router = Router(name='user callback router')


# handler for callback_data of record weight
@user_callback_router.callback_query(F.data == 'weight_btn_pressed')
async def process_weight_button(callback: CallbackQuery):
    await callback.message.edit_text( #type:ignore
        text='Send me your weight'
    )
    await callback.answer()


# handler for callback_data of record mesurement
@user_callback_router.callback_query(F.data == 'measure_btn_pressed')
async def process_measure_button(callback: CallbackQuery):
    await callback.message.edit_text(  #type:ignore
        text="Send me your measure"
    )
    await callback.answer()
