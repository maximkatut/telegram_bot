import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from dotenv import load_dotenv

from handlers.gpt_question import gpt_question_router
from handlers.gpt_quiz import gpt_quiz_router
from handlers.gpt_random import gpt_random_router
from handlers.gpt_talk import gpt_talk_router

commands = [
    types.BotCommand(command="start", description="Start the bot"),
    types.BotCommand(command="random", description="Random fact"),
    types.BotCommand(command="talk", description="Talk with famous person"),
    types.BotCommand(command="gpt", description="Ask GPT anything"),
    types.BotCommand(command="quiz", description="Play a quiz game"),
]

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

dp = Dispatcher()
dp.include_router(gpt_random_router)
dp.include_router(gpt_question_router)
dp.include_router(gpt_talk_router)
dp.include_router(gpt_quiz_router)


@dp.message(Command('start'))
async def command_start_handler(message: types.Message):
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    await message.answer(f'The list of commands:\n/start\n/random\n/gpt\n/talk\n/quiz')


async def main():
    bot = Bot(token=TELEGRAM_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.set_my_commands(commands)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
