from aiogram import types

from db import sql_worker
from localization import dictionary


async def help_command(message: types.Message):
    await message.answer(dictionary.help_message[sql_worker.get_language(message.from_user.id)])

