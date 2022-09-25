from platform import architecture
from re import T
import telebot

import time 

TOKEN = "5560881262:AAGcBr7b0oRtD13UgV1GIsdBNRINNO-uD-8"
bot = telebot.TeleBot(TOKEN)

def getargs(text):
    _args = text.split()[1:]
    return _args


@bot.message_handler(commands=["start"])
def sayhello(message):
    bot.send_message(message.chat.id,"Hello Thanks For Use My Bot.")


@bot.message_handler(commands=["help"])
def sayhelp(message):
    bot.send_message(message.chat.id,"hello broo")


@bot.message_handler(commands=["s","say"])
def texttospeech(message):
    args = getargs(message.text)
    text = " ".join(args[0:])
    try:
        bot.send_message(message.chat.id, text)
    except exception as e:
        bot.send_message(message.chat.id, f"there is fucked your msg")

while True:
    try:
        bot.polling()
        except:
            time.sleep(5)