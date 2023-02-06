from datetime import datetime, timedelta

from create_bot import bot
from aiogram import types

from chart import chart_worker
from db import sql_worker
from localization import dictionary

async def chart_command(message: types.Message):
    await message.answer(dictionary.create_chart[sql_worker.get_language(message.from_user.id)])

    day = str(datetime.now().strftime('%d.%m.%Y'))
    dt = datetime.strptime(str(day), '%d.%m.%Y')
    start = dt - timedelta(days=dt.weekday())
    end = start + timedelta(days=6)

    timestamp_start = sql_worker.get_timestamp(start.day, start.month, start.year, start.hour, start.minute, start.second)
    timestamp_end = sql_worker.get_timestamp(end.day, end.month, end.year, end.hour, end.minute, end.second)

    if chart_worker.make_chart(message.from_user.id, timestamp_start=timestamp_start, timestamp_end=timestamp_end):
        await bot.send_photo(message.from_user.id, photo=open(f'charts/{message.from_user.id}.png', 'rb'))
    else:
        await message.answer(dictionary.create_chart_error[sql_worker.get_language(message.from_user.id)])
