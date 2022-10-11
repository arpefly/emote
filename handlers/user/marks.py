from aiogram import types

from db import sql_worker


async def marks_handler(message: types.Message):
    sql_worker.write_mark(message.from_user.id, message.date.timestamp(), int(message.text.replace('0️⃣', '0')
                                                                                          .replace('1️⃣', '1')
                                                                                          .replace('2️⃣', '2')
                                                                                          .replace('3️⃣', '3')
                                                                                          .replace('4️⃣', '4')
                                                                                          .replace('5️⃣', '5')
                                                                                          .replace('6️⃣', '6')
                                                                                          .replace('7️⃣', '7')
                                                                                          .replace('8️⃣', '8')
                                                                                          .replace('9️⃣', '9')
                                                                                          .replace('🔟', '10')), '')
