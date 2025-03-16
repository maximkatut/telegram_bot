from aiogram.filters.callback_data import CallbackData


class MyCallback(CallbackData, prefix='my'):
    name: str


random_callback = MyCallback(name='random')
gpt_question_callback = MyCallback(name='gpt')
gpt_talk_callback = MyCallback(name='talk')
