from aiogram import Bot
from aiogram.types import Message
from parser.manage import get_csv


user_name = None  # its dummy username save


async def get_start(message: Message, bot: Bot):
    await bot.send_message(
        message.from_user.id,
        f"<b>Hello {message.from_user.first_name}, welcome to my bot\nPlease enter your name:</b>",
    )


async def get_text(message: Message):
    global user_name
    await message.answer("You send me a text message")
    if not user_name:
        user_name = message.text
        await message.answer(f"Your name {user_name} is saved")
    else:
        await message.answer(f"Dear, {user_name} parsing process is starts")
        try:
            result_csv: str = get_csv(message.text)
            print(result_csv)
            await message.answer(result_csv)
            # await message.answer_document(document=result_csv)
        except Exception as err:
            print(f"Get error: {err}")
