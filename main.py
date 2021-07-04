import os
import telebot
import random
import string
from dotenv import load_dotenv

load_dotenv("config.env")

bot_token = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(bot_token)

jokes = ["I was her semicolon but...    One day She decided to switch to Python.", "I'm on a seafood diet....   I see food and I wanna eat it.", "*Dad thinks you are gaming on the pc* Dad: Are you winning, son?  There is no winning with these syntax errors dad!"]

adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'fluffy', 'white', 'proud', 'brave']
nouns = ['apples', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck', 'panda', 'telephone', 'banana', 'teacher']
colours = ['blue', 'red', 'green', 'yellow', 'purple', 'magenta', 'black', 'white', 'orange', 'cyan', 'brown', 'silver', 'gold']

while True:
    for num in range(3):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0, 100)
        colour = random.choice(colours)
        special_char = random.choice(string.punctuation)

password = adjective + colour + noun + str(number) + special_char

@bot.message_handler(commands=["newpassword"])
def greet(message):
    bot.reply_to(message, "Your password is: %s" password)

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
def about(message):
    bot.send_message(message.chat.id, "Copyright EarthMapsPictures Corporation 2015-2021")
    bot.send_message(message.chat.id, "Developed by @alexthegreatish and @zakaryan2004")
    
    
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello I am EarthMapsPictures Bot. The Official EarthMapsPictures Website: https://earthmapspictures.weebly.com/")
    bot.send_message(message.chat.id, "Type /help to see what I can do!")
    
@bot.message_handler(commands=["help"])
def hello(message):
    bot.send_message(message.chat.id, "If you type /hello I will say hello.")
    bot.send_message(message.chat.id, "If If you type /greet I will greet you.")
    bot.send_message(message.chat.id, "If you are a Waka Masters member type /waka for a surprise.")
    bot.send_message(message.chat.id, "/about is about")
    bot.send_message(message.chat.id, "Also I like to make jokes.")
    bot.send_message(message.chat.id, "Upgrade to EMP Bot Premium to see this message.")
    bot.send_message(message.chat.id, "Upgrade to EMP Bot Premium to see this message.")
    bot.send_message(message.chat.id, "Answer?")
    bot.send_message(message.chat.id, "Oh yeah sorry. We dont have Premium its completely free to do anything with EMP Bot! That was a EA joke Pay to Play get it?")
    
@bot.message_handler(commands=["wakamasters"])
def wakamasters(message):
    bot.send_message(message.chat.id, "Waka Masters Forever!")
    
@bot.message_handler(commands=["joke"])
def joke(message):
    bot.send_message(message.chat.id, random.choice(jokes))
    
bot.polling()
