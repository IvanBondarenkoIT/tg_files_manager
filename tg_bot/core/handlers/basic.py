from aiogram import Bot
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
    await bot.send_message(
        message.from_user.id,
        f"<b>Hello {message.from_user.first_name}, welcome to my bot1</b>",
    )
    await message.answer(
        f"<s>Hello {message.from_user.first_name}, welcome to my bot2</s>"
    )
    await message.reply(
        f"<tg-spoiler>Hello {message.from_user.first_name}, welcome to my bot3</tg-spoiler>"
    )


async def get_photo(message: Message, bot: Bot):
    await message.answer(f"Great! Your sand image, i'm save it here!")
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, "photo.jpg")
