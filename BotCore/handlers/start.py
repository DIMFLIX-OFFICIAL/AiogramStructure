from aiogram import types
from aiogram.filters import Command

from General.loader import bot, dp


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text="hi"
    )
