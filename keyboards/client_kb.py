from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


b1 = KeyboardButton('/Начать')
b2 = KeyboardButton('/Отмена')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1, b2)
# kb_client.row(b1, b3)