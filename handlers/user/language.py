from aiogram import types

from db import sql_worker
from localization import dictionary


async def language_command(message: types.Message):
    if sql_worker.get_language(message.from_user.id) == 'ru':
        sql_worker.set_language(message.from_user.id, 'en')
        await message.answer(dictionary.language[sql_worker.get_language(message.from_user.id)])
    else:
        sql_worker.set_language(message.from_user.id, 'ru')
        await message.answer(dictionary.language[sql_worker.get_language(message.from_user.id)])
