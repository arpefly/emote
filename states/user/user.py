from aiogram.dispatcher.filters.state import State, StatesGroup


class SetCustomNames(StatesGroup):
    names = State()
