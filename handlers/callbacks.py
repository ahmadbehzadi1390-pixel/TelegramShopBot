from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.main_menu import main_menu
from keyboards.special_menu import special_menu

router = Router()


@router.callback_query(F.data == "special_services")
async def open_special_menu(callback: CallbackQuery):
    await callback.message.edit_reply_markup(
        reply_markup=special_menu
    )
    await callback.answer()
