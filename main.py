import os
import telebot
from dotenv import load_dotenv

load_dotenv("config.env")

bot_token = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=["greet"])
def greet(message):
    bot.reply_to(message, "Hey! What up?")


@bot.message_handler(commands=["emp"])
def emp(message):
    bot.send_message(message.chat.id, "earthmapspictures.weebly.com")


@bot.message_handler(commands=["hello"])
def hello(message):
    bot.send_message(message.chat.id, "Hello!")


@bot.message_handler(commands=["waka"])
def waka(message):
    bot.send_message(message.chat.id, "Waka Woka Wiki Weke Woko Weki Wake ...")


@bot.message_handler(commands=["about"])
def hello(message):
    bot.send_message(message.chat.id, "EarthMapsPictures Corporation!")


bot.polling()
