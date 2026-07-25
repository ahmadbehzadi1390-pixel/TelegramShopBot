from aiogram.fsm.state import State, StatesGroup


class StarsOrder(StatesGroup):
    waiting_for_username = State()
