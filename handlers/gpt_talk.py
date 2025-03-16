from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, FSInputFile

from handlers.gpt_question import gpt_question_router
from keyboards.question_keyboard import gpt_question_builder
from utils.callbacks import gpt_talk_callback
from utils.gpt_service import ChatGPTService
from utils.state import StateForm

gpt_talk_router = Router()
gpt_service = ChatGPTService()

PERSONS_PHOTOS = {
    'Elon Musk': 'musk.jpeg',
    'Leonardo da Vinci': 'vinci.jpeg',
    'Nikola Tesla': 'tesla.jpeg',
    'Theodore Roosevelt': 'roosevelt.jpg',
}


@gpt_talk_router.message(Command('talk'))
async def command_gpt(message: types.Message, state: FSMContext):
    await state.set_state(StateForm.choose_the_person)
    await message.answer("Choose the famous person you would like to talk to.",
                         reply_markup=ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     KeyboardButton(text="Elon Musk"),
                                     KeyboardButton(text="Leonardo da Vinci"),
                                     KeyboardButton(text="Nikola Tesla"),
                                     KeyboardButton(text="Theodore Roosevelt"),
                                 ]
                             ],
                             resize_keyboard=True,
                         ), )


@gpt_talk_router.message(StateForm.choose_the_person)
async def process_question(message: Message, state: FSMContext):
    await state.update_data(famous_person=message.text)
    gpt_service.set_system_message(
        f'You will be a famous person {message.text}. I would like to talk to yuo. I will ask some questions')
    photo = FSInputFile(f'assets/images/persons/{PERSONS_PHOTOS[message.text]}', 'person')
    await message.answer_photo(photo)
    await message.answer(f"My name is {message.text}. Please ask me anything!", reply_markup=ReplyKeyboardRemove())
    await state.set_state(StateForm.talk_with_person)


@gpt_talk_router.message(StateForm.talk_with_person)
async def process_question(message: Message, state: FSMContext):
    gpt_service.add_user_message(message.text)
    response = gpt_service.get_response()
    gpt_service.add_assistant_message(response)
    await message.answer(response, reply_markup=gpt_question_builder.as_markup())


@gpt_question_router.callback_query(gpt_talk_callback.filter(F.name == 'talk'))
async def callback_gpt_random(query: CallbackQuery, state: FSMContext):
    await state.clear()
    gpt_service.clear_history()
    await query.message.answer('OK, buy!')
