from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

import app.keyboards.startkb as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    user_name = message.from_user.first_name
    await message.answer(f'Hi, {user_name}! 👋\nSelect the option on the keyboard:', reply_markup=kb.startkb)