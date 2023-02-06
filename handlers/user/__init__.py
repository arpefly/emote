from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text

from .start import start_command
from .help import help_command
from .chart import chart_command
from .names import names_command
from .questions import questions_command
from .marks import marks_handler
from .notifications import notifications_command
from .language import language_command


def setup(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(chart_command, commands=['chart'])
    dp.register_message_handler(names_command, commands=['names'])
    dp.register_message_handler(questions_command, commands=['questions'])
    dp.register_message_handler(marks_handler, Text(equals=['0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']))
    dp.register_message_handler(notifications_command, commands=['notifications'])
    dp.register_message_handler(language_command, commands=['language'])
