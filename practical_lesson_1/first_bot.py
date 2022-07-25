import telebot
from telebot import types
from telebot.types import Message

import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(message: Message) -> None:
    """
    A handler for `/start` command.

    :param message: Message
    :return: None

    See: https://core.telegram.org/bots/api#message
    See: https://core.telegram.org/bots/api#replykeyboardmarkup
    """
    start_menu = types.ReplyKeyboardMarkup(True, True)
    start_menu.row("Begin")
    bot.send_message(
        chat_id=message.chat.id,
        text="Welcome!\n"
             "This is my first bot in telegram!\n"
             "I hope that you will be satisfied ;)",
        reply_markup=start_menu,
    )


@bot.message_handler(content_types=['text'])
def text_handler_begin(message: Message) -> None:
    """
    A handler for `Begin` text typing.

    :param message: Message
    :return: None

    See: https://core.telegram.org/bots/api#message
    """
    if message.text == "Begin":
        send = bot.send_message(
            chat_id=message.chat.id,
            text="What is your name?)",
        )
        # TODO is it possible to do it without 3 handler functions?
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
