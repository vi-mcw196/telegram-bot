import aiogram.utils.markdown as fmt
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from practical_lesson_2.app.keyboards.main_keyboard import main_keyboard, main_with_contacts_keyboard
from practical_lesson_2.app.keyboards.start_menu import start_menu_keyboard
from practical_lesson_3.app.keyboards.contacts_keyboard_inline import contacts_keyboard_inline
from practical_lesson_4.app.keyboards.contacts_keyboard_inline_creator import contacts_keyboard_inline_creator
from practical_lesson_4.static.img.images import PERSON1_PHOTO, PERSON3_PHOTO, PERSON2_PHOTO
from practical_lesson_5.static.img.images import FITNESS_PHOTO


async def cmd_start(message: types.Message):
    await message.answer(
        text="Привет! Наш бот поможет тебе узнать больше о нашем фитнес-клубе! \n"
             "Если хочешь узнать подробнее о создателе меня - пиши /bot",
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


async def about_fitness_club(message: types.Message):
    await message.answer_photo(
        photo=FITNESS_PHOTO,
        caption="Наш клуб работает с 2005 года. \n"
                "За это время мы успели открыть 300+ клубов по всей стране. \n"
                "Наши тренера - люди, занимающиеся в данной сфере от 10 лет и больше! \n"
                "Наш главный офис находится по адресу: \n"
                " Pl. Grunwaldzki 22 50-363 Wrocław \n\n"
                "Ждем с нетерпением вас в наших клубах!"
                "Работает круглосуточно!",
        reply_markup=main_keyboard,
    )


async def price(message: types.Message):
    await message.answer(
        text="Прайс на наши услуги: \n\n"
             "Сольные занятие – от 69$\\month \n"
             "Групповые занятия – от 80$\\month \n"
             "Занятия с тренером – от 110$\\month \n"
             f"Полный прайс можно посмотреть по ссылке ниже:"
             f"https://fitness-academy.com.pl/",
        reply_markup=main_with_contacts_keyboard,
        parse_mode=types.ParseMode.HTML
    )


async def out_fitness_couches(message: types.Message):
    await message.answer_photo(
        photo=PERSON1_PHOTO,
        caption="Старший тренер. \n"
                "Анна Темьянова, 27 лет \n"
                "Тренер в клубе уже 10 лет",
    )
    await message.answer_photo(
        photo=PERSON2_PHOTO,
        caption="Старший тренер в области спорт-лифтинга. \n"
                "Сергей Семьян, 32 лет \n"
                "Работает в клубе уже 15 лет",
    )
    await message.answer_photo(
        photo=PERSON3_PHOTO,
        caption="Стажер-тренер женский. \n"
                "Татьяна Васильевна, 35 лет \n"
                "Работает в клубе уже 3 месяца",
        reply_markup=main_keyboard,
    )


async def contacts(message: types.Message):
    await message.answer(
        text="Наш главный офис находится по адресу: Pl. Grunwaldzki 22 50-363 Wrocław \n"
             "- Тел. +48570424477 \n"
             "- Наш менеджер в телеграмме: @def196 \n"
             "- Наш Instagram: https://instagram.com/fitness-academy \n\n"
             "- Чтобы связаться с разработчиком бота выполните команду: /bot",
        reply_markup=contacts_keyboard_inline,
    )


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_bot, commands="bot", state="*")
    dp.register_message_handler(main_menu, Text(equals="Главное меню", ignore_case=True), state="*")
    dp.register_message_handler(about_fitness_club, Text(equals="О клубе", ignore_case=True), state="*")
    dp.register_message_handler(price, Text(equals="Прайс", ignore_case=True), state="*")
    dp.register_message_handler(out_fitness_couches, Text(equals="Наши тренера", ignore_case=True), state="*")
    dp.register_message_handler(contacts, Text(equals="Контакты", ignore_case=True), state="*")
