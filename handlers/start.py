from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards.stars_menu import stars_menu
from keyboards.special_menu import special_menu

router = Router()


class StarsOrder(StatesGroup):
    waiting_for_username = State()


# باز کردن منوی استارز
@router.callback_query(F.data == "stars")
async def stars_menu_open(callback: CallbackQuery):
    await callback.message.edit_text(
        "⭐ لطفاً یکی از پلن‌های استارز را انتخاب کنید:",
        reply_markup=stars_menu
    )
    await callback.answer()


# بازگشت به خدمات ویژه
@router.callback_query(F.data == "back_special")
async def back_special(callback: CallbackQuery):
    await callback.message.edit_text(
        "⭐ خدمات ویژه",
        reply_markup=special_menu
    )
    await callback.answer()


# انتخاب پلن استارز
@router.callback_query(F.data.startswith("buy_stars_"))
async def buy_stars(callback: CallbackQuery, state: FSMContext):
    amount = callback.data.replace("buy_stars_", "")

    await state.update_data(amount=amount)

    await callback.message.edit_text(
        f"⭐ سفارش {amount} استار\n\n"
        "لطفاً آیدی تلگرام خود را ارسال کنید.\n\n"
        "مثال:\n"
        "@username"
    )

    await state.set_state(StarsOrder.waiting_for_username)
    await callback.answer()


# دریافت آیدی
@router.message(StarsOrder.waiting_for_username)
async def get_username(message: Message, state: FSMContext):
    data = await state.get_data()

    amount = data["amount"]
    username = message.text

    await message.answer(
        "✅ سفارش شما ثبت شد.\n\n"
        f"⭐ تعداد استار: {amount}\n"
        f"👤 آیدی: {username}\n\n"
        "سفارش برای ادمین ارسال خواهد شد."
    )

    await state.clear()
