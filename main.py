import telebot

import parsing

tracking = 'np00000000866099npi'
url = 'https://novaposhta.ua/tracking/international/cargo_number/{}'.format(tracking)

token = '874887236:AAGeU93uqdoe0GuecyHvMBVRd10wznxX9dk'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, parsing.get_html(url))
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'the END')


bot.polling()
