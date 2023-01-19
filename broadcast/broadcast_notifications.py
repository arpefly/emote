import logging
import asyncio

from create_bot import bot
from aiogram.utils import exceptions

from db import sql_worker


async def send_message(chat_id: int, text: str, disable_notification: bool = True) -> bool:
    """
    Safe messages sender

    :param chat_id: Id пользователя
    :param text: текст, который будет отправлен пользователю
    :param disable_notification:
    :return:
    """

    try:
        await bot.send_message(chat_id, text, disable_notification=disable_notification)
    except exceptions.BotBlocked:
        sql_worker.write_error(chat_id, False, 'BotBlocked')
    except exceptions.ChatNotFound:
        sql_worker.write_error(chat_id, False, 'ChatNotFound')
    except exceptions.UserDeactivated:
        sql_worker.write_error(chat_id, False, 'UserDeactivated')
    except exceptions.RetryAfter as ex:
        logging.error(f"Target [ID:{chat_id}]: Flood limit is exceeded. Sleep {ex.timeout} seconds.")
        await asyncio.sleep(ex.timeout)
        return await send_message(chat_id, text)  # Recursive call
    except Exception as ex:
        sql_worker.write_error(chat_id, False, str(ex))
    else:
        return True
    return False


async def start_broadcaster():
    """
    Рассылка уведомлений
    """

    try:
        for chat_id in sql_worker.get_users_to_broadcasr():
            await send_message(chat_id, 'Как настроение ?')
            await asyncio.sleep(.05)  # 20 messages per second (Limit: 30 messages per second)
    finally:
        pass
