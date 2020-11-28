import telebot
from telebot import types
from emoji import emojize
from test import *
TOKEN = "1316052122:AAFHsy300Q2Cj18CRtnd8na7oiP1NyJhHvM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id,'Привет, маленький засранец :)')



@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')

    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')



    elif message.text.lower() == 'фейсбук':
        bot.send_message(message.chat.id, fcbook())
    elif message.text.lower() == 'инстаграм':
        bot.send_message(message.chat.id, inst())
    else:
        bot.send_message(message.chat.id, 'а всё уже')
@bot.message_handler(func=lambda message: True)
def any_message(message):
    bot.reply_to(message, format(message.text))

bot.polling()
