import os  # Импорт os для использования переменной среды

from aiogram import Bot, Dispatcher

bot = Bot(token=os.getenv('EMOTION_API_TOKEN'))  # Создание экземпляра бота с токеном с виртуальной среды
dp = Dispatcher(bot=bot)
