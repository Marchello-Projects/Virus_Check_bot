from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

startkb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='❔ help'), KeyboardButton(text='🦠 scan')]
], resize_keyboard=True)