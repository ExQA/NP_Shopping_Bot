import telebot
from telebot import types
import parsing
from random import choice
from emoji import emojize
from utility import SMILE

from mongodb import (
    mdb,
    search_or_save_user,
    # save_user_anketa,
    # save_picture_name,
    # save_file_id,
    # save_like_dislike,
)


# tracking = 'np00000000866099npi'
# url = 'https://novaposhta.ua/tracking/international/cargo_number/{}'.format(tracking)

# t.me/NP_Shopping_Bot

token = "874887236:AAGeU93uqdoe0GuecyHvMBVRd10wznxX9dk"
bot = telebot.TeleBot(token)

# функция sms() будет вызвана пользователем при отправке команды start,
# внутри функции будет описана логика при ее вызове
def sms(bot, update):
    user = search_or_save_user(
        mdb, bot.effective_user, bot.message
    )  # получаем данные из базы данных
    print(user)
    smile = emojize(choice(SMILE), use_aliases=True)  # для ответа добавили emoji
    print(
        "Кто-то отправил команду /start. Что мне делать?"
    )  # вывод сообщения в консоль при отправки команды /start
    bot.message.reply_text(
        "Здравствуйте, {}! \nПоговорите со мной {}!".format(
            bot.message.chat.first_name, smile
        )
    )  # отправляем ответ


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, sms(), "Привет, ты написал мне /start")



@bot.message_handler(content_types=["text"])
def send_text(message):

    track_details = parsing.parse(message.text)

    data = (
        "Current place: " + "\n"
        "Time: " + track_details["date"] + "\n"
        "Status: " + track_details["status"] + "\n"
        "Country: " + track_details["country"]
    )

    bot.send_message(message.chat.id, data, sms())


@bot.callback_query_handler(func=lambda c: True)
def answer(c):
    key = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Text of button", callback_data="cat")
    key.add(button)


bot.polling()
