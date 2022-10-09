import asyncio
import aioschedule
import os  # Импорт os для использования переменной среды

from aiogram import Bot, Dispatcher
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from db import sql_worker
from broadcast import broadcast_text
import handlers.admin  # Ипорт handlers

storage = MemoryStorage()
bot = Bot(token=os.getenv('EMOTION_API_TOKEN'))  # Создание экземпляра бота с токеном с виртуальной среды
dp = Dispatcher(bot=bot, storage=storage)


async def scheduler():
    aioschedule.every(1).minutes.do(broadcast_text.start_broadcaster)

    while 1:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    handlers.user.setup(dp)  # Регистрация handlers для пользователей
    sql_worker.sql_start()  # Подключение к базе данных
    asyncio.create_task(scheduler())  # Подпить на рассылку каждый час для всех пользователей

    print('bot is online')


async def on_shutdown(_):
    aioschedule.clear()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
