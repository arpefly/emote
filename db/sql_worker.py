import datetime
import sqlite3 as sql


base = sql.connect("db.db")
cur = base.cursor()


def sql_connect():
    """
    Подключение к db.db
    """

    print('Successful connection to the db.db')

def is_user_in_db(chat_id: int) -> bool:
    """
    Содержит ли db.db пользователя с id chat_id ?

    :param chat_id: chat_id пользователя
    :return:
        True: если пользователь есть в db.db
        False: если пользователя нет в db.db
    """

    if cur.execute('SELECT COUNT(chat_id) FROM users WHERE chat_id is ?', (chat_id,)).fetchone()[0] == 1:
        return True
    else:
        return False

def add_user_to_db(chat_id: int, username: str, fisrt_name: str, last_name: str) -> None:
    """
    Добавить пользователя в db.db

    :param chat_id: chat_id пользователя
    :param username: username пользователя
    :param fisrt_name: fisrt_name пользователя
    :param last_name: last_name пользователя
    """

    base.execute('INSERT INTO users VALUES(?, ?, ?, ?, ?, ?)', (chat_id, username, fisrt_name, last_name, True, 'OK'))
    base.commit()

def get_all_users() -> list:
    """
    Получить все chat_id из db.db

    :return: list со всеми chat_id в db.db
    """

    users_list = cur.execute('SELECT chat_id FROM users').fetchall()
    return [item[0] for item in users_list]

def get_users_to_broadcasr() -> list:
    """
    Получить всех пользователей, которые не заблокировали бота или не забанены или аккаунт ещё существует

    :return: list с chat_id которым можено отправить уведолмление
    """

    users_list = cur.execute('SELECT chat_id FROM users WHERE can_send').fetchall()
    return [item[0] for item in users_list]

def write_error(chat_id: int, can_send:bool, error_type: str):
    """
    Записать ошибку из-за которой бот не может отправить сообщение

    :param chat_id: chat_id пользователя
    :param can_send: Может ли бот отправить сообщение пользователю
    :param error_type: Тип ошибки
    """

    base.execute('UPDATE users SET can_send = ?, error_type = ? WHERE chat_id is ?', (can_send, error_type, chat_id))
    base.commit()

def is_send_message_possible(chat_id:int) -> bool:
    """
    Может ли бот отправить уведомлене ?

    :param chat_id: chat_id пользователя, которого нужно проверить
    :return:
        True: если при отправке последнего уведомления не происходило ошибки (кроме exceptions.RetryAfter)
        False: если при отправке последнего уведомления произошла ошикбка (кроме exceptions.RetryAfter)
    """

    can_send:bool = bool(cur.execute('SELECT can_send FROM users WHERE chat_id is ?', (chat_id,)).fetchone()[0])
    base.commit()

    return can_send

def write_mark(chat_id: int, timestamp: float, mark: int, comment: str):
    """
    Записать оценку настроения в db.db

    :param chat_id: chat_id пользователя
    :param timestamp: отметка времени
    :param mark: оценка настроения
    :param comment: комментарий к оценке
    """

    base.execute('INSERT INTO notes VALUES(?, ?, ?, ?)', (chat_id, timestamp, mark, ''))
    base.commit()

def get_marks(chat_id: int, timestamp_start: int, timestamp_end: int) -> list:
    """
    Получить все оценки настроения в заданном диапазоне или

    :param chat_id: chat_id пользователя
    :param timestamp_start: начало диапазона выборки
    :param timestamp_end: конец диапазона выборки
    :return: lsit c времеными метками и оценками настроения вида [(timestamp1, mark1), (timestamp2, mark2), ...]
    """
    marks_lsit = list(cur.execute('SELECT timestamp, mark FROM notes WHERE chat_id == ? and timestamp BETWEEN ? and ?', (chat_id, timestamp_start, timestamp_end)).fetchall())
    return marks_lsit

def get_timestamp(day, month, year, hour, minute, second):
    return datetime.datetime.timestamp(datetime.datetime(year, month, day, hour, minute, second))

def get_datetime(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%d.%m.%Y %H:%M:%S')
