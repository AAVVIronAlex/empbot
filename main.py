import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['greet'])
def greet(message):
  bot.reply_to(message, "Hey! What up?")

@bot.message_handler(commands=['emp'])
def emp(message):
  bot.send_message(message.chat.id, "earthmapspictures.weebly.com")

@bot.message_handler(commands=['hello'])
def hello(message):
  bot.send_message(message.chat.id, "Hello!")

@bot.message_handler(commands=['waka'])
def waka(message):
  bot.send_message(message.chat.id, "Waka Woka Wiki Weke Woko Weki Wake ...")

@bot.message_handler(commands=['about'])
def hello(message):
  bot.send_message(message.chat.id, "EarthMapsPictures Corporation!")

bot.polling()