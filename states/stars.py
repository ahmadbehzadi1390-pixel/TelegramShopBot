from aiogram.fsm.state import State, StatesGroup


class StarsOrder(StatesGroup):
    waiting_for_user_id = State()
    waiting_for_quantity = State()
    waiting_for_confirm = State()
