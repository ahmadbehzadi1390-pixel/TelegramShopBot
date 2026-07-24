from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data == "stars")
async def stars_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        "⭐ خرید استارز تلگرام\n\n"
        "یکی از پلن‌های زیر را انتخاب کنید:\n\n"
        "⭐ 50 استار\n"
        "⭐ 100 استار\n"
        "⭐ 250 استار\n"
        "⭐ 500 استار\n"
        "⭐ 1000 استار"
    )
    await callback.answer()
