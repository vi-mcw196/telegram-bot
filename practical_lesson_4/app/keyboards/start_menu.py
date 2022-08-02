from aiogram import types

start_menu = [
    "Кто Я?",
    "Портфолио",
    "Прайс",
    "Условия работы",
    "Контакты",
]

start_menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
start_menu_keyboard.add(*start_menu)
