from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router(name='user callback router')


# handler for callback_data of record weight
@router.callback_query(F.data == 'weight_btn_pressed')
async def process_weight_button(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Send me your weight'
    )


# handler for callback_data of record mesurement
@router.callback_query(F.data == 'measure_btn_pressed')
async def process_measure_button(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Send me your measure"
    )
