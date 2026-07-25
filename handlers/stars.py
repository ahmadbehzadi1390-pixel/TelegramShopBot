from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.main_menu import main_menu

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        "👋 سلام!\n\n"
        "به ربات خدمات مجازی خوش اومدی.",
        reply_markup=main_menu
    )
