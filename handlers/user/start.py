from aiogram import types

from db import sql_worker
from keyboards import marks
from localization import dictionary


async def start_command(message: types.Message):
    if not sql_worker.is_user_in_db(message.from_user.id):
        sql_worker.add_user_to_db(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name, 'ru' if message.from_user.language_code == 'ru' else 'en')
    await message.answer(dictionary.greeting[sql_worker.get_language(message.from_user.id)], reply_markup=marks.marks_kb)

    if not sql_worker.is_send_message_possible(message.from_user.id):
        sql_worker.write_error(message.from_user.id, True, 'OK')
