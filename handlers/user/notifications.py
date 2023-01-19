from aiogram import types

from db import sql_worker

async def notifications_command(message: types.Message):
    if sql_worker.is_send_message_possible(message.from_user.id):
        sql_worker.write_error(message.from_user.id, False, 'Disable')
        await message.answer('Уведомления выключены.')
    else:
        sql_worker.write_error(message.from_user.id, True, 'OK')
        await message.answer('Уведомления включены.')
