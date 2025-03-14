from aiogram import Router, types
from aiogram.filters import Command

from utils.gpt_service import ChatGPTService

gpt_random_router = Router()
gpt_service = ChatGPTService()

@gpt_random_router.message(Command('random'))
async def command_gpt_random(message: types.Message):
    message_answer = await message.answer("A random fact is loading...")
    reply = gpt_service.get_random_fact_response()
    await message_answer.edit_text(reply)
