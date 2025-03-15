from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery

from keyboards.random_keyboard import random_builder
from utils.callbacks import random_callback
from utils.gpt_service import ChatGPTService

gpt_random_router = Router()
gpt_service = ChatGPTService()


@gpt_random_router.message(Command('random'))
async def command_gpt_random(message: types.Message):
    message_answer = await message.answer("A random fact is loading...")
    reply = gpt_service.get_random_fact_response()
    await message_answer.edit_text(reply, reply_markup=random_builder.as_markup())


@gpt_random_router.callback_query(random_callback.filter(F.name == 'random'))
async def callback_gpt_random(query: CallbackQuery):
    reply = gpt_service.get_random_fact_response()
    await query.message.answer(reply)
