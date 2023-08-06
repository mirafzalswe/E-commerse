from aiogram.dispatcher.filters.state import State, StatesGroup

class St_Customser(StatesGroup):
    name = State()
    address = State()
    phone = State()


class SellerState(StatesGroup):
    name = State()
    address = State()
    phone = State()

