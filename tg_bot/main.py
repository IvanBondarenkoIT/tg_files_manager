from aiogram import Bot, Dispatcher
from aiogram.types import Message
from core.handlers.basic import get_start

import asyncio
import logging


from config import tg_api_token, my_user_id


async def start_bot(bot: Bot):
    await bot.send_message(my_user_id, text="Hello. Bot is starts")


async def stop_bot(bot: Bot):
    await bot.send_message(my_user_id, text="Hello. Bot is closed")


async def start():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    )
    bot = Bot(token=tg_api_token, parse_mode="HTML")

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
