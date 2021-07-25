import os
import telebot
from dotenv import load_dotenv

load_dotenv("config.env")

bot_token = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(bot_token)
