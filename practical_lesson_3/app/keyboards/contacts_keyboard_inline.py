from aiogram import types


inst_button = types.InlineKeyboardButton(
    text="Инстраграм",
    url="https://instagram.com/fitness-academy",
    callback_data="contact-inst"
)

telegram_button = types.InlineKeyboardButton(
    text="Telegram",
    url="https://t.me/def196",
    callback_data="contact-telegram"
)

contacts_keyboard_inline = types.InlineKeyboardMarkup()
contacts_keyboard_inline.add(inst_button, telegram_button)
