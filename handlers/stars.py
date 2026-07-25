from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.stars_menu import stars_menu
from keyboards.special_menu import special_menu

router = Router()


@router.callback_query(F.data == "stars")
async def open_stars(callback: CallbackQuery):
    await callback.message.edit_reply_markup(
        reply_markup=stars_menu
    )
    await callback.answer()


@router.callback_query(F.data == "back_special")
async def back_special(callback: CallbackQuery):
    await callback.message.edit_reply_markup(
        reply_markup=special_menu
    )
    await callback.answer()


@router.callback_query(F.data.startswith("stars_"))
async def stars_order(callback: CallbackQuery):
    amount = callback.data.split("_")[1]

    await callback.message.answer(
        f"✅ سفارش {amount} استار ثبت شد.\n\n"
        "💳 لطفاً پرداخت را انجام دهید.\n"
        "بعد از پرداخت سفارش شما توسط ادمین انجام می‌شود."
    )

    await callback.answer()
