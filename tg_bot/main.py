from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
from core.handlers.basic import get_start, get_text

import asyncio
import logging
from core.settings import settings

# from aiogram.dispatcher.filters import ContentTypesFilter


async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Hello. Bot is starts")
    # await bot.send_message(text="Please enter your name:")


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Hello. Bot is closed")


async def start():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    )
    bot = Bot(token=settings.bots.bot_token, parse_mode="HTML")

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start, F.text == "/start")
    dp.message.register(get_text, F.text)

    # dp.message.register(get_start)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
