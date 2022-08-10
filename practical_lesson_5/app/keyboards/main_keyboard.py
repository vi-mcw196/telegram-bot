from aiogram import types

main = ["Главное меню"]
main_with_contacts = ["Главное меню", "Контакты"]

main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add(*main)

main_with_contacts_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
main_with_contacts_keyboard.add(*main_with_contacts)
