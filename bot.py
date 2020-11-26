import telebot
from telebot import types
from emoji import emojize
from test import *
TOKEN = "1316052122:AAFHsy300Q2Cj18CRtnd8na7oiP1NyJhHvM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id,'Привет, маленький засранец :)')

# @bot.message_handler(commands=['help'])
# def any_message(message):
#     caption = 'Какие глазки! :eyes:'
#     bot.reply_to(message, caption.format(message.text))
#

# @bot.message_handler(commands=['photo'])
# def process_photo_command(message):
#     caption = 'Какие глазки! :eyes:'
#     bot.reply_to(message.from_user.id,
#                          caption=emojize(caption),CAT_BIG_EYES,
#                          reply_to_message_id=message.message_id)

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    #elif message.text.lower() == 'я тебя люблю':
     #   bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBD9ZfEJCVXn_KSm7COrSSzFY15DU3CAACdQEAAnvAfRNZSgGUv-3IZhoE')
    elif message.text.lower() == 'фейсбук':
        bot.send_message(message.chat.id, fcbook())
   # elif message.text.lower() == 'лина':
     #   bot.send_message(message.chat.id, 'Лина, йди у сраку')
    #elif message.text.lower() == 'английские маты':
      #  bot.send_message(message.chat.id, '\nAss \nFaggot\nDick sucker\nHooker')
   # elif message.text.lower() == 'русские маты':
      #  bot.send_message(message.chat.id, '\nЖопа \nМудак\nЧленосос\nШлюха')
    #elif message.text.lower() == 'итальянские маты':
      #  bot.send_message(message.chat.id, '\nCulo \nStronzo\nSucchiacazzi\nPuttana')
    #elif message.text.lower() == 'немецкие маты':
       # bot.send_message(message.chat.id, '\nArsch \nArschloch\nSchwanzlutscher\nHure')
    else:
        bot.send_message(message.chat.id, 'а всё уже')
@bot.message_handler(func=lambda message: True)
def any_message(message):
    bot.reply_to(message, format(message.text))

bot.polling()
