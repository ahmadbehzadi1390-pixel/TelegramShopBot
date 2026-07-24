from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

stars_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="⭐ 50 استار",
                callback_data="stars_50"
            )
        ],
        [
            InlineKeyboardButton(
                text="⭐ 100 استار",
                callback_data="stars_100"
            )
        ],
        [
            InlineKeyboardButton(
                text="⭐ 250 استار",
                callback_data="stars_250"
            )
        ],
        [
            InlineKeyboardButton(
                text="⭐ 500 استار",
                callback_data="stars_500"
            )
        ],
        [
            InlineKeyboardButton(
                text="⭐ 1000 استار",
                callback_data="stars_1000"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔙 بازگشت",
                callback_data="back_special"
            )
        ]
    ]
)
