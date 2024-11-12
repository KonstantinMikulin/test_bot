import logging

from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from bot.keyboards import url_keyboard, create_records_keyboard
from bot.FSM import FSMAddWeightRecord
from bot.db.requests import add_weight

logger = logging.getLogger(__name__)

# creating router`s onject
user_router = Router(name='user router')


# /cancel commands for default state
@user_router.message(Command(commands="cancel"), StateFilter(default_state))
async def cmd_cancel_default(message: Message):
    await message.answer('Nothing to cancel. You are out of FSM')


# /cancel if user in some state 
@user_router.message(Command(commands="cancel"), ~StateFilter(default_state))
async def cmd_cancel_state(message: Message, state: FSMContext):
    await message.answer("You are cancel FSM")
    # reset state and clear any received data
    await state.clear()


# command /weight 'only' for user
@user_router.message(Command(commands='weight'), StateFilter(default_state))
async def cmd_weight(message: Message, state: FSMContext, admin_id):
    await message.answer('Send your weight, please')
    # setup state to waiting for weight data
    await state.set_state(FSMAddWeightRecord.fill_weight)
    
    
# handler if weight was sent correct
@user_router.message(StateFilter(FSMAddWeightRecord.fill_weight), F.text.isdigit())
async def process_weight_sent(
    message: Message,
    state: FSMContext,
    session: AsyncSession
):
    # store weight into storage
    await state.update_data(weight=int(message.text)) # type:ignore
    
    context_data = await state.get_data()
    weight = int(context_data.get('weight'))  # type:ignore

    # add weight to db
    await add_weight(
        session=session,
        telegram_id=message.from_user.id,  # type:ignore
        weight=weight,
    )
    # stop FSM
    await state.clear()
    # send message abour success
    await message.answer(f"Your weight: {weight} kg added to database, user!")


# handler if weight was sent not correct
@user_router.message(StateFilter(FSMAddWeightRecord.fill_weight))
async def warning_not_weight(message: Message):
    await message.answer('Send correct data, please')


# command for /diet for everyone
@user_router.message(Command(commands='diet'))
async def cmd_diet(message: Message):
    await message.answer(
        text='Here are your food and goal',
        reply_markup=url_keyboard
    )


# commands for /record for everyone
@user_router.message(Command(commands='record'))
async def cmd_record(message: Message):
    await message.answer(
        text='What do you want to write down?',
        reply_markup=create_records_keyboard()
    )
