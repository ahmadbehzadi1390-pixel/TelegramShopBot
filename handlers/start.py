from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()


class StarsOrder(StatesGroup):
    waiting_for_username = State()


@router.callback_query(F.data.startswith("buy_stars_"))
async def buy_stars(callback: CallbackQuery, state: FSMContext):
    amount = callback.data.split("_")[-1]

    await state.update_data(amount=amount)

    await callback.message.edit_text(
        f"⭐ سفارش {amount} استار\n\n"
        "لطفاً آیدی تلگرام خود را ارسال کنید.\n\n"
        "مثال:\n"
        "@username"
    )

    await state.set_state(StarsOrder.waiting_for_username)
    await callback.answer()


@router.message(StarsOrder.waiting_for_username)
async def get_username(message: Message, state: FSMContext):
    data = await state.get_data()

    amount = data["amount"]
    username = message.text

    await message.answer(
        "✅ سفارش شما ثبت شد.\n\n"
        f"⭐ تعداد استار: {amount}\n"
        f"👤 آیدی: {username}\n\n"
        "ادمین به زودی سفارش شما را بررسی می‌کند."
    )

    await state.clear()
