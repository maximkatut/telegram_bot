from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.callbacks import random_callback

one_more_button = InlineKeyboardButton(text='One more fact', callback_data=random_callback.pack())

random_builder = InlineKeyboardBuilder([
    [one_more_button]
])
