import logging
import asyncio
from aiogram import Bot, Dispatcher

from handlers import (
    start,
    default,
    size_qr,
)

from data import TOKEN



logger = logging.getLogger(__name__)
logging.basicConfig(
    level="INFO",
    format="%(name)s : %(asctime)s : %(levelname)s : %(message)s"
)

async def main():
    bot = Bot(token=TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(        
        start.router,
        size_qr.router,
        default.router
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())