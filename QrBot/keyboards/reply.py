from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# start.py
size = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="small"), KeyboardButton(text="medium"), KeyboardButton(text="large")
    ]
], resize_keyboard=True
)