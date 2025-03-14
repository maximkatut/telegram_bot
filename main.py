import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

dp = Dispatcher()


@dp.message(Command('start'))
async def command_start_handler(message: types.Message):
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message(Command('hello'))
async def command_hello(message: types.Message):
    await message.answer("Hello, let's start!")


async def main():
    bot = Bot(token=TELEGRAM_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
