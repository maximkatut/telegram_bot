from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.callbacks import gpt_question_callback

finish_button = InlineKeyboardButton(text='Finish', callback_data=gpt_question_callback.pack())

gpt_question_builder = InlineKeyboardBuilder([
    [finish_button]
])
