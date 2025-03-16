import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from dotenv import load_dotenv

from handlers.gpt_question import gpt_question_router
from handlers.gpt_random import gpt_random_router

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

dp = Dispatcher()
dp.include_router(gpt_random_router)
dp.include_router(gpt_question_router)


@dp.message(Command('start'))
async def command_start_handler(message: types.Message):
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    await message.answer(f'The list of commands:\n/start\n/random\n/gpt')


async def main():
    bot = Bot(token=TELEGRAM_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
