from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from practical_lesson_2.app.keyboards.main_keyboard import main_keyboard, main_with_contacts_keyboard
from practical_lesson_2.app.keyboards.start_menu import start_menu_keyboard
from practical_lesson_3.app.keyboards.contacts_keyboard_inline import contacts_keyboard_inline
from practical_lesson_3.static.img.images import PORTFOLIO_PHOTO


async def cmd_start(message: types.Message):
    await message.answer(
        text="Привет! Ты попал в бот-визитку. \n"
             "Здесь ты найдешь пример моих работ и подробную информацию обо мне!",
        reply_markup=start_menu_keyboard
    )


async def about_me(message: types.Message):
    await message.answer(
        text="Привет! Меня зовут Виктор. Мне 19 лет. Готов сделать любого бота на заказ за короткий промежуток времени",
        reply_markup=main_keyboard,
    )


async def main_menu(message: types.Message):
    await message.answer(
        text="Cтартовое меню! \n",
        reply_markup=start_menu_keyboard,
    )


async def portfolio(message: types.Message):
    await message.answer_photo(photo=PORTFOLIO_PHOTO)
    await message.answer(
        text="Мои последние боты: \n"
             "- @my_bot \n"
             "- @second_my_bot \n",
        reply_markup=main_keyboard,
    )


async def price(message: types.Message):
    await message.answer(
        text="Цена бота начинается от 200$, и зависит от сложности и количества аудитории \n",
        reply_markup=main_with_contacts_keyboard,
    )


async def way_of_working(message: types.Message):
    await message.answer(
        text="Работаю по предоплате. Оцениваю риски и сложность бота, даю вам оценку времени и стоимость"
             "за мою работу. \n\n"
             "После вашего согласия и оплаты приступаю к работе. \n\n"
             "Обычно спустя 4-5 дней предоставляю первый прототип.",
        reply_markup=main_keyboard,
    )


async def contacts(message: types.Message):
    await message.answer(
        text="Со мной связаться можно с помощью: \n\n"
             "- telegram: @def196 \n"
             "- gmail: def196@gmail.com",
        reply_markup=contacts_keyboard_inline,
    )


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(main_menu, Text(equals="Главное меню", ignore_case=True), state="*")
    dp.register_message_handler(about_me, Text(equals="Кто Я?", ignore_case=True), state="*")
    dp.register_message_handler(portfolio, Text(equals="Портфолио", ignore_case=True), state="*")
    dp.register_message_handler(price, Text(equals="Прайс", ignore_case=True), state="*")
    dp.register_message_handler(way_of_working, Text(equals="Условия работы", ignore_case=True), state="*")
    dp.register_message_handler(contacts, Text(equals="Контакты", ignore_case=True), state="*")
