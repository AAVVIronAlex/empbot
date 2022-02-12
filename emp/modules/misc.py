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
    "happy",
    "gross",
    "faster",
    "dusty",
    "cool",
    "messy",
    "mischievous",
    "garrulous",
    "long",
    "cold",
    "hot",
    "warm",
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
    "proud",
    "beutiful",
]
NOUNS = [
    "apples",
    "dog",
    "cat",
    "skyscraper",
    "house",
    "garden",
    "pen",
    "pencil",
    "car",
    "music",
    "computer",
    "mouse"
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
    "aqua",
    "aquamarine",
]

# Add a calculator

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
    
# newpassword 2.0
@bot.message_handler(commands=["newpasswordultra"])
def newpassword_ultra_2(message):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-=<>,.?/;:"

    string = lower + upper + numbers + symbols
    length = 16
    password = "".join(random.sample(string, length))
    bot.send_message(message.chat.id, "Your password is: " + password)