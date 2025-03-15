from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.callbacks import random_callback

one_more_button = InlineKeyboardButton(text='Press for one more', callback_data=random_callback.pack())

random_builder = InlineKeyboardBuilder([
    [one_more_button]
])
