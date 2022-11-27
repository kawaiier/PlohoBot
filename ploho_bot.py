import telebot
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')
CHANNEL = "-1001686742290"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет! Пойдешь сегодня в Плохо?\nПрисылай мне текст для публкации в @plohopodslushano")

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.send_message(message.chat.id, "Присылай мне текст для публкации в @plohopodslushano")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(CHANNEL, message.text)

@bot.message_handler(content_types=['photo'])
def echo_photo(message):
    bot.send_photo(CHANNEL, message.photo[0].file_id)

bot.infinity_polling()