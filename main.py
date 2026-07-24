import asyncio
import os

from aiohttp import web
from aiogram import Bot, Dispatcher

from config.settings import BOT_TOKEN
from handlers.start import router as start_router
from handlers.callbacks import router as callback_router


async def health_check(request):
    return web.Response(text="Bot is running")


async def run_web_server():
    app = web.Application()
    app.router.add_get("/", health_check)

    runner = web.AppRunner(app)
    await runner.setup()

    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)

    await site.start()


async def main():
    await run_web_server()

    bot = Bot(token=BOT_TOKEN)

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(callback_router)

    print("✅ Bot Started Successfully")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
