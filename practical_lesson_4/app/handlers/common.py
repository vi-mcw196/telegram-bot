import aiogram.utils.markdown as fmt
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from practical_lesson_2.app.keyboards.main_keyboard import main_keyboard, main_with_contacts_keyboard
from practical_lesson_2.app.keyboards.start_menu import start_menu_keyboard
from practical_lesson_3.app.keyboards.contacts_keyboard_inline import contacts_keyboard_inline
from practical_lesson_4.app.keyboards.contacts_keyboard_inline_creator import contacts_keyboard_inline_creator
from practical_lesson_4.static.img.images import PERSON1_PHOTO, PERSON3_PHOTO, PERSON2_PHOTO


async def cmd_start(message: types.Message):
    await message.answer(
        text="Привет! Наш бот поможет тебе узнать нас лучше.",
        reply_markup=start_menu_keyboard
    )


async def cmd_bot(message: types.Message):
    await message.answer(
        text="Привет! Меня зовут Виктор. Мне 19 лет. Готов сделать любого бота на заказ за короткий промежуток времени",
        reply_markup=contacts_keyboard_inline_creator
    )


async def main_menu(message: types.Message):
    await message.answer(
        text="Cтартовое меню! \n",
        reply_markup=start_menu_keyboard,
    )


async def service_centre(message: types.Message):
    await message.answer(
        text="Наш сервис работает с 2005 года. \n"
             "За это время мы успели обслужить миллион машин разных марок и моделей. \n"
             "Используем только оригинальные запчасти. \n\n"
             "С уважением, владелец сервиса Виктор!",
        reply_markup=main_keyboard,
    )


async def about_cars(message: types.Message):
    await message.answer(
        text="Мы работаем с такими марками: \n"
             "- BMW \n"
             "- AUDI \n"
             "- MINI \n"
             "- Mercedes \n"
             "- Volkswagen \n",
        reply_markup=main_keyboard,
    )


async def price(message: types.Message):
    await message.answer(
        text="Прайс на наши услуги: \n\n"
             "Диагностика – от 99$ \n"
             "Предпродажная подготовка – от 139$ \n"
             "Развал схождения – 20$ \n"
             "Замена масла – 40$ \n"
             f"{fmt.hide_link('https://speed.bosch-service.pl/pl')}"
             f"Полный прайс можно посмотреть по ссылке ниже:",
        reply_markup=main_with_contacts_keyboard,
        parse_mode=types.ParseMode.HTML
    )


async def way_of_working(message: types.Message):
    await message.answer(
        text="В работу принимаем: \n"
             "- Чистые автомобили \n"
             "- Автомобили которые не числятся в угоне",
        reply_markup=main_keyboard,
    )


async def about_us(message: types.Message):
    await message.answer_photo(
        photo=PERSON1_PHOTO,
        caption="Глава автосервиса. \n"
                "Анна Темьянова, 27 лет \n"
                "Работает в фирме 10 лет",
    )
    await message.answer_photo(
        photo=PERSON2_PHOTO,
        caption="Старший помощник автосервиса. \n"
                "Сергей Семьян, 32 лет \n"
                "Работает в фирме 5 лет",
    )
    await message.answer_photo(
        photo=PERSON3_PHOTO,
        caption="Зам Главы автосервиса. \n"
                "Татьяна Васильевна, 35 лет \n"
                "Работает в фирме 15 лет",
        reply_markup=main_keyboard,
    )


async def contacts(message: types.Message):
    await message.answer(
        text="Мы находимся по адресу г. Москва. Ул. Ленина 1. \n"
             "- Тел. +7459656559 \n"
             "- Наш менеджер в телеграмме: @def196 \n"
             "- Наш Instagram: https://instagram.com/auto_service \n\n"
             "- Чтобы связаться с разработчиком бота выполните команду: /bot",
        reply_markup=contacts_keyboard_inline,
    )


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_bot, commands="bot", state="*")
    dp.register_message_handler(main_menu, Text(equals="Главное меню", ignore_case=True), state="*")
    dp.register_message_handler(service_centre, Text(equals="Об автосервисе", ignore_case=True), state="*")
    dp.register_message_handler(about_cars, Text(equals="С какими машинами работаем", ignore_case=True), state="*")
    dp.register_message_handler(price, Text(equals="Прайс", ignore_case=True), state="*")
    dp.register_message_handler(way_of_working, Text(equals="Условия работы", ignore_case=True), state="*")
    dp.register_message_handler(about_us, Text(equals="Наша команда", ignore_case=True), state="*")
    dp.register_message_handler(contacts, Text(equals="Контакты", ignore_case=True), state="*")
