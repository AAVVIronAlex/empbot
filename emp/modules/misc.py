from emp import bot
import random
import string
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
