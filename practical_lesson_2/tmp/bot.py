import telebot
from telebot import types
from telebot.types import Message
from languages import en, ru

import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(message: Message) -> None:
    """
    A handler for `/start` command.

    :param message: Message
    :return: None

    See: https://core.telegram.org/bots/api#message
    See: https://core.telegram.org/bots/api#inlinekeyboardmarkup
    """
    keyboard = [
        [
            types.InlineKeyboardButton(text="en", callback_data='en'),
            types.InlineKeyboardButton(text="ru", callback_data='ru'),
        ]
    ]
    languages = types.InlineKeyboardMarkup(keyboard=keyboard)

    bot.send_message(
        chat_id=message.chat.id,
        text="Welcome!\n"
             "This is my portfolio bot in telegram!\n"
             "Please choose language you prefer!",
        reply_markup=languages,
    )


@bot.message_handler(content_types=['text'])
def text_handler_language(message: Message) -> None:
    """
    A handler for `Begin` text typing.

    :param message: Message
    :return: None

    See: https://core.telegram.org/bots/api#message
    """
    send = None
    language_dict = dict()

    if message.text == "en":
        send = bot.send_message(
            chat_id=message.chat.id,
            text="Ok! You are welcome!",
        )
        language_dict = en.txt
    elif message.text == "ru":
        send = bot.send_message(
            chat_id=message.chat.id,
            text="Язык успешно выбран!\n"
                 "Добро пожаловать!",
        )
        language_dict = ru.txt
    bot.register_next_step_handler(send, text_handler_begin, language_dict)


@bot.message_handler(content_types=['text'])
def text_handler_begin(message: Message, txt: dict[str]) -> None:
    """
    A handler for `Begin` text typing.

    :param txt: dict[str]
    :param message: Message
    :return: None

    See: https://core.telegram.org/bots/api#message
    """
    start_menu = types.ReplyKeyboardMarkup(True, True)
    start_menu.row(
        txt["Who_Am_I"],
        txt["Portfolio"],
        txt["Price"],
        txt["Way_Of_Working"],
        txt["Find_Me"],
    )
    send = bot.send_message(
        chat_id=message.chat.id,
        text=txt["Explore"]
    )
    bot.register_next_step_handler(send, text_handler_age)


def text_handler_age(message: Message) -> None:
    """
    A handler for asking age in a user.

    :param message: Message
    :return: None

    See: https://core.telegram.org/bots/api#message
    """
    send = bot.send_message(
        chat_id=message.chat.id,
        text=f"Nice to meet {message.text}\n"
             f"How old are you?",
    )
    bot.register_next_step_handler(send, text_handler_learning_level)


def text_handler_learning_level(message: Message) -> None:
    """
    A handler for asking learning skills in a user.

    :param message: Message
    :return: None

    See: https://core.telegram.org/bots/api#message
    See: https://core.telegram.org/bots/api#replykeyboardmarkup
    """
    choice = types.ReplyKeyboardMarkup(True, False)
    choice.row(
        "Stranger",
        "Beginner",
        "Experienced",
        "Master",
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=f"Can you also answer how do you feel in development of telegram bots?",
        reply_markup=choice,
    )


bot.polling()
