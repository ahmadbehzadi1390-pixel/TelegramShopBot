from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.stars_menu import stars_menu
from keyboards.special_menu import special_menu

router = Router()


# باز کردن منوی استارز
@router.callback_query(F.data == "stars")
async def open_stars(callback: CallbackQuery):
    await callback.message.edit_text(
        "⭐ لطفاً تعداد استار موردنظر را انتخاب کنید:",
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


# ثبت سفارش
@router.callback_query(F.data.startswith("stars_"))
async def buy_stars(callback: CallbackQuery):
    amount = callback.data.split("_")[1]

    await callback.message.edit_text(
        f"""✅ سفارش شما ثبت شد.

⭐ تعداد استار: {amount}

لطفاً منتظر پیام ادمین باشید."""
    )

    await callback.answer("سفارش ثبت شد ✅")
