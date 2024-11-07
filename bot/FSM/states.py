from aiogram.fsm.state import State, StatesGroup


class FSMAddWeightRecord(StatesGroup):
    fill_weight = State()
