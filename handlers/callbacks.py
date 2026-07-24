from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.main_menu import main_menu
from keyboards.special_menu import special_menu
from keyboards.stars_menu import stars_menu

router = Router()


# =========================
# خدمات ویژه
# =========================
@router.callback_query(F.data == "special_services")
async def open_special_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        "⭐ خدمات ویژه",
        reply_markup=special_menu
    )
    await callback.answer()


# =========================
# استارز
# =========================
@router.callback_query(F.data == "stars")
async def open_stars_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        "⭐ یکی از پلن‌های استارز را انتخاب کنید:",
        reply_markup=stars_menu
    )
    await callback.answer()


# =========================
# بازگشت از خدمات ویژه
# =========================
@router.callback_query(F.data == "back_main")
async def back_main(callback: CallbackQuery):
    await callback.message.edit_text(
        "👋 سلام!\n\nبه ربات خدمات مجازی خوش اومدی.",
        reply_markup=main_menu
    )
    await callback.answer()


# =========================
# بازگشت از استارز
# =========================
@router.callback_query(F.data == "back_special")
async def back_special(callback: CallbackQuery):
    await callback.message.edit_text(
        "⭐ خدمات ویژه",
        reply_markup=special_menu
    )
    await callback.answer()
