from aiogram import types

from db import sql_worker
from keyboards import marks


async def start_command(message: types.Message):
    if not sql_worker.is_user_in_db(message.from_user.id):
        sql_worker.add_user_to_db(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
    await message.answer('Превет 👋\n\nЯ буду вести твой журнал настроения.', reply_markup=marks.marks_kb)

    if not sql_worker.is_send_message_possible(message.from_user.id):
        sql_worker.write_error(message.from_user.id, True, 'OK')
