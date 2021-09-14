from emp import bot
import random
import string
from pyrogram import  Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from html import escape

# CONSTANTS
JOKES = [
    "I was her semicolon but...    One day She decided to switch to Python.",
    "I'm on a seafood diet....   I see food and I wanna eat it.",
    "*Dad thinks you are gaming on the pc* Dad: Are you winning, son?  There is"
    " no winning with these syntax errors dad!",
]
ADJECTIVES = [
    "sleepy",
    "slow",
    "smelly",
    "wet",
    "fat",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "fluffy",
    "white",
    "proud",
    "brave",
]
NOUNS = [
    "apples",
    "dinosaur",
    "ball",
    "toaster",
    "goat",
    "dragon",
    "hammer",
    "duck",
    "panda",
    "telephone",
    "banana",
    "teacher",
]
COLOURS = [
    "blue",
    "red",
    "green",
    "yellow",
    "purple",
    "magenta",
    "black",
    "white",
    "orange",
    "cyan",
    "brown",
    "silver",
    "gold",
]


@bot.message_handler(commands=["newpassword"])
def newpassword(message):
    adjective = random.choice(ADJECTIVES)
    noun = random.choice(NOUNS)
    number = random.randrange(0, 100)
    colour = random.choice(COLOURS)
    special_char = random.choice(string.punctuation)

    password = adjective + colour + noun + str(number) + special_char

    bot.reply_to(
        message,
        f"Your password is: <code>{escape(password)}</code>",
        parse_mode="HTML",
    )


@bot.message_handler(commands=["waka"])
def waka(message):
    bot.send_message(message.chat.id, "Waka Woka Wiki Weke Woko Weki Wake ...")


@bot.message_handler(commands=["wakamasters"])
def wakamasters(message):
    bot.send_message(message.chat.id, "Waka Masters Forever!")


@bot.message_handler(commands=["joke"])
def joke(message):
    bot.send_message(message.chat.id, random.choice(JOKES))

@bot.message_handler(commands=["alex"])
def alex(message):
    bot.send_message(message.chat.id, "Alex has lost over 500GBs of data and is trying to recover it he is busy don't bother him for free recovery software please DM him on any platform. Thanks.")

    @bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    TEXT = "Hai {} \n\n**I Am Password Generator Bot. I Can Generate Strong Passwords At Your Wish Length (Max. 84).** \n\nFor Know More /help"
    BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton("Channel 🔰", url = "https://telegram.me/EKBOTZ_UPDATE"),InlineKeyboardButton("Support Group ⭕️", url = "https://telegram.me/ekbotz_support")],[InlineKeyboardButton("Repo 🗂️", url = "https://github.com/M-fazin/Password-Generator-Bot"),InlineKeyboardButton("Deploy 🗃️", url = "https://heroku.com/deploy?template=https://github.com/M-fazin/Password-Generator-Bot")],[InlineKeyboardButton("Developer 💡", url = "https://github.com/M-fazin/")]])
    await update.reply_text(
        text=TEXT.format(update.from_user.mention),
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )

    #Password Generator Rev.2
    
@bot.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    HELP = "Hello, I am EMP Bot password creator Rev. 2.0. \nMaximum Send Digit limit a random password will be generated in that limit. \nAllowed Digits Till 84"
   
    await update.reply_text(
        text=HELP.format(update.from_user.mention),
        reply_markup=HELP_BUTTON,
        disable_web_page_preview=True,
        quote=True
        )
	
@bot.on_message(filters.private & filters.text)
async def password(bot, message):
    password = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+"
    try:
       limit = int(message.text)
    except:
       pass    
    if limit >= 85 or limit <= 0:
        text = "Sorry... Failed To Create Password Because Limit is 1 to 84"
    else:
        randomValue = random.sample(password, limit)
        randomValue = "".join(randomValue)
        text = f"**Your Password Generated Succesfully.** \nYour Password Limit : `{limit}`. \nPassword 👇 :- \n`{randomValue}` "
      
    await message.reply_text(text, True)
	

			
bot.run()
