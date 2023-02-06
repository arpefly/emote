from aiogram import types

from db import sql_worker
from localization import dictionary

async def notifications_command(message: types.Message):
    if sql_worker.is_send_message_possible(message.from_user.id):
        sql_worker.write_error(message.from_user.id, False, 'Disable')
        await message.answer(dictionary.notifications_off[sql_worker.get_language(message.from_user.id)])
    else:
        sql_worker.write_error(message.from_user.id, True, 'OK')
        await message.answer(dictionary.notifications_on[sql_worker.get_language(message.from_user.id)])
