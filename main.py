import telebot
import parsing
import config
from loguru import logger
# tracking = 'np00000000866099npi'
# url = 'https://novaposhta.ua/tracking/international/cargo_number/{}'.format(tracking)

# t.me/NP_Shopping_Bot
from database import subscribe, add_tracking

token = config.API_TOKEN
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    subscribe(message.chat.id)
    bot.send_message(message.chat.id, 'You subscribe')


@bot.message_handler(content_types=['text'])
def send_text(message):
    track_details = parsing.parse(message.text)
    bot.send_message(message.chat.id, track_details)


bot.polling()
