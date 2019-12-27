import telebot
from telebot import types
import parsing

# tracking = 'np00000000866099npi'
# url = 'https://novaposhta.ua/tracking/international/cargo_number/{}'.format(tracking)

# t.me/NP_Shopping_Bot

token = '874887236:AAGeU93uqdoe0GuecyHvMBVRd10wznxX9dk'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


@bot.message_handler(content_types=['text'])
def send_text(message):
    track_details = parsing.parse(message.text)

    data = ('Time: ' + track_details['date'] + '\n' 
            'Status: ' + track_details['status'] + '\n' 
            'Country: ' + track_details['country']
            )

    bot.send_message(message.chat.id, data)


@bot.callback_query_handler(func=lambda c: True)
def answer(c):
    key = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='Text of button', callback_data='cat')
    key.add(button)


bot.polling()
