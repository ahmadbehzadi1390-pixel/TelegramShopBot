from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

special_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🌟 استارز تلگرام",
                callback_data="stars"
            )
        ],
        [
            InlineKeyboardButton(
                text="💎 پرمیوم تلگرام",
                callback_data="premium"
            )
        ],
        [
            InlineKeyboardButton(
                text="🚀 بوست گروه و کانال",
                callback_data="boost"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔙 بازگشت",
                callback_data="back_main"
            )
        ]
    ]
)
