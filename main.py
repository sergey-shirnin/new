from config import token
from telebot import TeleBot

# instance of the class
bot = TeleBot(token)


@bot.message_handler(commands=['help', 'start'])
def send_message(message):
    bot.reply_to(message, 'hello I am your bot')


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, 'What a photo!!!')


bot.infinity_polling()
