from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from keyboards.stars_menu import stars_menu
from keyboards.special_menu import special_menu
from states.stars import StarsOrder

router = Router()


@router.callback_query(F.data == "stars")
async def open_stars(callback: CallbackQuery):
    await callback.message.edit_text(
        "⭐ لطفاً تعداد استار موردنظر را انتخاب کنید:",
        reply_markup=stars_menu
    )
    await callback.answer()


@router.callback_query(F.data == "back_special")
async def back_special(callback: CallbackQuery):
    await callback.message.edit_text(
        "🌟 خدمات ویژه",
        reply_markup=special_menu
    )
    await callback.answer()


@router.callback_query(F.data.startswith("stars_"))
async def choose_stars(callback: CallbackQuery, state: FSMContext):
    amount = callback.data.split("_")[1]

    await state.update_data(amount=amount)
    await state.set_state(StarsOrder.waiting_for_user_id)

    await callback.message.edit_text(
        f"⭐ شما {amount} استار را انتخاب کردید.\n\n"
        "📩 لطفاً Telegram ID عددی خود را ارسال کنید."
    )

    await callback.answer()


@router.message(StarsOrder.waiting_for_user_id)
async def receive_user_id(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(
            "❌ لطفاً فقط شناسه عددی تلگرام را ارسال کنید."
        )
        return

    data = await state.get_data()
    amount = data["amount"]

    await state.clear()

    await message.answer(
        "✅ سفارش شما ثبت شد.\n\n"
        f"⭐ تعداد استار: {amount}\n"
        f"🆔 Telegram ID: {message.text}\n\n"
        "💳 مرحله پرداخت را در قدم بعدی اضافه می‌کنیم."
                      )
