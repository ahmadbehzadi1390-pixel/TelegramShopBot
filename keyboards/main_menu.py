from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="⭐ خدمات ویژه",
                callback_data="special_services"
            )
        ],
        [
            InlineKeyboardButton(
                text="💰 سفارش ارز تلگرام",
                callback_data="telegram_currency"
            )
        ],
        [
    InlineKeyboardButton(
        text="👥 سفارش ممبر",
        callback_data="members"
    ),
    InlineKeyboardButton(
        text="🎁 گیفت تلگرام",
        callback_data="gift"
    )
],
        [
            InlineKeyboardButton(
                text="👀 ویو",
                callback_data="views"
            ),
            InlineKeyboardButton(
                text="❤️ ری‌اکشن",
                callback_data="reactions"
            )
        ],
        [
            InlineKeyboardButton(
                text="👤 حساب کاربری",
                callback_data="profile"
            ),
            InlineKeyboardButton(
                text="📜 قوانین",
                callback_data="rules"
            )
        ],
        [
            InlineKeyboardButton(
                text="💳 افزایش موجودی",
                callback_data="deposit"
            ),
            InlineKeyboardButton(
                text="☎️ پشتیبانی",
                callback_data="support"
            )
        ]
    ]
)
