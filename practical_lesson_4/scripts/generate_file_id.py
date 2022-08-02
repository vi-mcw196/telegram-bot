import telebot
import requests

from practical_lesson_3.app.config_reader import load_config

config = load_config(r"C:\Users\38066\PycharmProjects\telegram-bots\practical_lesson_3\config\bot.ini")
token = config.tg_bot.token

bot = telebot.TeleBot(token=config.tg_bot.token)


@bot.message_handler(content_types=['text'])
def repeat_all_message(message):
    print(message.text)
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=["document", "video", "audio"])
def handle_files(message):
    document_id = message.document.file_id
    file_info = bot.get_file(document_id)
    print(document_id)
    print(f'http://api.telegram.org/file/bot{token}/{file_info.file_path}')
    bot.send_message(message.chat.id, document_id)


@bot.message_handler(content_types=["photo"])
def handle_files(message):
    photo_id = message.photo[-1].file_id
    file_info = bot.get_file(photo_id)
    print(photo_id)
    print(f'http://api.telegram.org/file/bot{token}/{file_info.file_path}')
    bot.send_message(message.chat.id, photo_id)


if __name__ == '__main__':
    bot.polling(none_stop=True)
