from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

png = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="PNG", callback_data="png")
        ]
    ]
)