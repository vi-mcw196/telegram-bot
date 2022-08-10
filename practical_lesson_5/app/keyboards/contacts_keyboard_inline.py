from aiogram import types

gmail_button = types.InlineKeyboardButton(
    text="Gmail.com",
    url="mailto:def196@gmail.com",
    callback_data="contact-gmail"
)

telegram_button = types.InlineKeyboardButton(
    text="Telegram",
    url="https://t.me/def196",
    callback_data="contact-telegram"
)

contacts_keyboard_inline = types.InlineKeyboardMarkup()
contacts_keyboard_inline.add(gmail_button, telegram_button)
