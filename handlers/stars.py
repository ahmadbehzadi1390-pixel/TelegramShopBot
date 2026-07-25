from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data == "stars")
async def open_stars(callback: CallbackQuery):
    from keyboards.stars_menu import stars_menu

    await callback.message.edit_text(
        "⭐ لطفاً تعداد استار موردنظر را انتخاب کنید:",
        reply_markup=stars_menu
    )
    await callback.answer()


@router.callback_query(F.data == "back_special")
async def back_special(callback: CallbackQuery):
    from keyboards.special_menu import special_menu

    await callback.message.edit_text(
        "🌟 خدمات ویژه",
        reply_markup=special_menu
    )
    await callback.answer()


@router.callback_query(F.data.startswith("stars_"))
async def buy_stars(callback: CallbackQuery):
    amount = callback.data.split("_")[1]

    await callback.message.edit_text(
        f"✅ شما {amount} استار را انتخاب کردید.\n\n"
        "💳 مرحله بعد: پرداخت (بعداً اضافه می‌کنیم)."
    )
    await callback.answer()
