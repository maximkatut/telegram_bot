from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, FSInputFile

from keyboards.question_keyboard import gpt_question_builder
from utils.callbacks import gpt_question_callback
from utils.gpt_service import ChatGPTService

gpt_question_router = Router()
gpt_service = ChatGPTService()


class Form(StatesGroup):
    waiting_for_question = State()


@gpt_question_router.message(Command('gpt'))
async def command_gpt(message: types.Message, state: FSMContext):
    photo = FSInputFile('assets/images/gpt.png', 'gpt')
    await message.answer_photo(photo)
    await message.answer("Ask GPT anything.")
    await state.set_state(Form.waiting_for_question)


@gpt_question_router.message(Form.waiting_for_question)
async def process_question(message: Message, state: FSMContext):
    user_question = message.text
    gpt_service.add_user_message(user_question)
    response = gpt_service.get_response()
    gpt_service.add_assistant_message(response)
    await message.answer(response, reply_markup=gpt_question_builder.as_markup())


@gpt_question_router.callback_query(gpt_question_callback.filter(F.name == 'gpt'))
async def callback_gpt_random(query: CallbackQuery, state: FSMContext):
    await state.clear()
    await query.message.answer('OK, buy!')
