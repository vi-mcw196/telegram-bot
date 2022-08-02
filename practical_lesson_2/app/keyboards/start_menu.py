from aiogram import types

start_menu = [
    "Об автосервисе",
    "С какими машинами работаем",
    "Прайс",
    "Условия работы",
    "Наша команда",
    "Контакты",
]

start_menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
start_menu_keyboard.add(*start_menu)
