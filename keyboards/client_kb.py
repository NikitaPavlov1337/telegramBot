from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


b2 = KeyboardButton('/Начать')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b2)
# kb_client.row(b1, b3)