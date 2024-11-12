import logging

from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from sqlalchemy.ext.asyncio import AsyncSession

from bot.FSM import FSMAddMeasurmentRecord
from bot.db import add_waist, add_hips, add_bicep

logger = logging.getLogger(__name__)

# creating router`s onject
user_measure_router = Router(name="user measurements router")


# command /measure 'only' for user
@user_measure_router.message(
    Command(commands="measure"), StateFilter(default_state)
)
async def cmd_measure(message: Message, state: FSMContext):
    await message.answer("Send your waist, please")
    # setup state to waiting for waist measurements data
    await state.set_state(FSMAddMeasurmentRecord.fill_waist)


# handler if waist`s data was sent correct
@user_measure_router.message(
    StateFilter(FSMAddMeasurmentRecord.fill_waist), F.text.isdigit()
)
async def process_waist_sent(
    message: Message,
    state: FSMContext,
    session: AsyncSession
):
    # store waist in storage
    await state.update_data(waist=message.text)  # type:ignore
    
    # set next state
    await state.set_state(FSMAddMeasurmentRecord.fill_hips)
    
    # send message
    await message.answer(f"Your waist: {message.text} cm added to database, user!\n"
                         f"Send your hips now")


# handler if hips` data was sent correct
@user_measure_router.message(StateFilter(FSMAddMeasurmentRecord.fill_hips), F.text.isdigit())
async def process_hips_sent(
    message: Message,
    state: FSMContext,
    session: AsyncSession
):
    # store waist in storage
    await state.update_data(hips=message.text)  # type:ignore

    # set next state
    await state.set_state(FSMAddMeasurmentRecord.fill_bicep)

    # send message
    await message.answer(
        f"Your hips: {message.text} cm added to database, user!\n"
        f"Send your bicep now"
    )


# handler if bicep`s data was sent correct
@user_measure_router.message(StateFilter(FSMAddMeasurmentRecord.fill_bicep), F.text.isdigit())
async def process_bicep_sent(
    message: Message,
    state: FSMContext,
    session: AsyncSession
):
    # store waist in storage
    await state.update_data(bicep=message.text)  # type:ignore

    # set next state
    await state.set_state(FSMAddMeasurmentRecord.fill_done)

    # get data from sorage
    context_data = await state.get_data()
    waist = int(context_data.get("waist")) # type:ignore
    print(f'Type of waist {waist} is: {type(waist)}')
    hips = int(context_data.get("hips")) # type:ignore
    bicep = int(context_data.get("bicep")) # type:ignore

    # add all records to db
    await add_waist(
        session=session,
        telegram_id=message.from_user.id, # type:ignore
        waist=waist,
    )
    
    await add_hips(
        session=session,
        telegram_id=message.from_user.id, # type:ignore
        hips=hips,
    )
    
    await add_bicep(
        session=session,
        telegram_id=message.from_user.id,  # type:ignore
        bicep=bicep,
    )
    
    # stop FSM
    await state.clear()

    # send message
    await message.answer(
        f"Your bicep: {message.text} cm added to database, user!\n"
        f"Thank you"
    )
    

# handler if data of waist, hips or bicep was sent not correct
@user_measure_router.message(
    StateFilter(
        FSMAddMeasurmentRecord.fill_waist,
        FSMAddMeasurmentRecord.fill_hips,
        FSMAddMeasurmentRecord.fill_bicep,
    )
)
async def warning_not_correct_mesurment(message: Message):
    await message.answer("Send correct data, please")
