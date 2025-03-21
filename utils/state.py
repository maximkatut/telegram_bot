from aiogram.fsm.state import StatesGroup, State


class StateForm(StatesGroup):
    waiting_for_question = State()
    talk_with_person = State()
    choose_the_person = State()
    famous_person = State()
    choose_topic = State()
