import asyncio

from aiogram import Bot, Dispatcher

from config.settings import BOT_TOKEN
from handlers.start import router as start_router
from handlers.callbacks import router as callback_router


async def main():
    bot = Bot(token=BOT_TOKEN)

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(callback_router)

    print("✅ Bot Started Successfully")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
  