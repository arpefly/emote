import asyncio

import aioschedule

from aiogram import executor

from create_bot import dp
from db import sql_worker
from broadcast import broadcast_notifications
import handlers  # Ипорт handlers


async def scheduler():
    """
    Планировщик рассылки уведомлений
    """

    aioschedule.every(5).seconds.do(broadcast_notifications.start_broadcaster)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    handlers.user.setup(dp)  # Регистрация handlers для пользователей
    sql_worker.sql_connect()  # Подключение к базе данных
    asyncio.create_task(scheduler())  # Подпить на рассылку каждый час для всех пользователей

    print('bot is online')

async def on_shutdown(_):
    aioschedule.clear()


executor.start_polling(dp, skip_updates=False, on_startup=on_startup, on_shutdown=on_shutdown)
