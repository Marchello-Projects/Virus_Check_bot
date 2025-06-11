import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers import routers

load_dotenv()

bot = Bot(token=os.getenv('BOT_API'))  
dp = Dispatcher()

for r in routers:
    dp.include_router(r)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())