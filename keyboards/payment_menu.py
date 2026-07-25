from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

payment_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="💳 کارت بانکی",
                callback_data="pay_card"
            )
        ],
        [
            InlineKeyboardButton(
                text="💎 ارز دیجیتال",
                callback_data="pay_crypto"
            )
        ],
        [
            InlineKeyboardButton(
                text="❌ لغو سفارش",
                callback_data="cancel_order"
            )
        ]
    ]
)
