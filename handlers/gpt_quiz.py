from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup, FSInputFile, \
    InlineKeyboardMarkup, InlineKeyboardButton

from utils.gpt_service import ChatGPTService
from utils.state import StateForm

gpt_quiz_router = Router()
gpt_service = ChatGPTService()

topics_list = ["Science", "History", "Geography", "Literature", "Sports", "Movies", "Music", "Technology"]
topic_keyboard_buttons = [[KeyboardButton(text=topic)] for topic in topics_list]

option_map = {
    "option_a": "A",
    "option_b": "B",
    "option_c": "C",
    "option_d": "D"
}
inline_kb_list = [
    [
        InlineKeyboardButton(text=value, callback_data=key) for key, value in option_map.items()
    ],
    [
        InlineKeyboardButton(text="Finish", callback_data="finish"),
        InlineKeyboardButton(text="Change topic", callback_data="change_topic"),
    ]
]
inline_kb = InlineKeyboardMarkup(inline_keyboard=inline_kb_list)


@gpt_quiz_router.message(Command('quiz'))
async def command_quiz(message: types.Message, state: FSMContext):
    await state.set_state(StateForm.choose_topic)
    photo = FSInputFile('assets/images/quiz.webp', 'quiz')
    await message.answer_photo(photo)

    await message.answer("Choose the topic which you would like to play",
                         reply_markup=ReplyKeyboardMarkup(
                             keyboard=topic_keyboard_buttons,
                             resize_keyboard=True,
                             one_time_keyboard=True
                         ), )


@gpt_quiz_router.message(StateForm.choose_topic)
async def process_question(message: Message, state: FSMContext):
    gpt_service.set_system_message(
        'I want to play the quiz game.'
        'Create a question that tests general knowledge across the topic I will provide.'
        'I will give you an answer and after give me another question and show the total score, for example 1/10.'
        'The answers will be A,B,C,D.'
        'Do not make any markups to the text.'
        'There should be 10 questions total.'
    )
    gpt_service.add_user_message(message.text)
    response = gpt_service.get_response()
    gpt_service.add_assistant_message(response)
    await message.answer(response, reply_markup=inline_kb)


@gpt_quiz_router.callback_query(lambda c: c.data in ["option_a", "option_b", "option_c", "option_d"])
async def process_callback_answer(query: CallbackQuery):
    if query.data in option_map:
        gpt_service.add_user_message(option_map[query.data])
        response = gpt_service.get_response()
        gpt_service.add_assistant_message(response)
        await query.message.answer(response, reply_markup=inline_kb)
    await query.answer()


@gpt_quiz_router.callback_query(lambda c: c.data == "finish")
async def process_callback_finish(query: CallbackQuery, state: FSMContext):
    await state.clear()
    gpt_service.clear_history()
    await query.message.answer('OK, buy!')
    await query.answer()


@gpt_quiz_router.callback_query(lambda c: c.data == "change_topic")
async def process_callback_change_topic(query: CallbackQuery, state: FSMContext):
    await state.clear()
    gpt_service.clear_history()
    await command_quiz(query.message, state)
    await query.answer()
