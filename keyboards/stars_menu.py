from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.stars_menu import stars_menu
from keyboards.special_menu import special_menu

router = Router()


@router.callback_query(F.data == "stars")
async def open_stars_menu(callback: CallbackQuery):
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

    await callback.message.edit_text(
        f"⭐ سفارش {amount} استار تلگرام\n\n"
        "🔄 این بخش در حال تکمیل است..."
    )
    await callback.answer()
