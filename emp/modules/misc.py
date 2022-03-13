from emp import bot
import random
import string
from html import escape
import datetime

# CONSTANTS
JOKES = [
    "I was her semicolon but...    One day She decided to switch to Python.",
    "I'm on a seafood diet....   I see food and I wanna eat it.",
    "*Dad thinks you are gaming on the pc* Dad: Are you winning, son?  There is"
    " no winning with these syntax errors dad!",
    "What’s the best thing about Switzerland? I don’t know, but the flag is a big plus.",
    "What is an astronaut’s favorite part on a computer? The space bar."
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
    "extreme",
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

@bot.message_handler(commands = ["newpassword"])
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


@bot.message_handler(commands = ["waka"])
def waka(message):
    bot.send_message(message.chat.id, "Waka Woka Wiki Weke Woko Weki Wake ...")


@bot.message_handler(commands = ["wakamasters"])
def wakamasters(message):
    bot.send_message(message.chat.id, "Waka Masters Forever!")


@bot.message_handler(commands = ["joke"])
def joke(message):
    bot.send_message(message.chat.id, random.choice(JOKES))

@bot.message_handler(commands = ["alex"])
def alex(message):
    bot.send_message(message.chat.id, "Alex has lost over 500GBs of data and is trying to recover it he is busy don't bother him for free recovery software please DM him on any platform. Thanks.")
    
@bot.message_handler(commands = ["random"])
def random_message(message):
    bot.send_message(message.chat.id, "Mary, my brother, my age is blowing in my chest. I must be from the beginning, but you are who I am I don't know what to say about me, but I don't want to tell you anything but me There is no problem, but you are not")
    
@bot.message_handler(commands = ["general"])
def general(message):
    bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=w0m0hTrtlWM&t=28s")

@bot.message_handler(commands = ["sati"])
def sati(message):
    bot.send_message(message.chat.id, "https://instagram.fevn1-4.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s640x640/261826967_121435980347228_7475127980642126532_n.webp.jpg?_nc_ht=instagram.fevn1-4.fna.fbcdn.net&_nc_cat=108&_nc_ohc=S5zcTTdxYdUAX_-Njsc&edm=AABBvjUBAAAA&ccb=7-4&ig_cache_key=MjcxODU2ODc0ODY5OTExNDY2Ng%3D%3D.2-ccb7-4&oh=00_AT-A1IwJlnfoqJlIMzROd7sJ21lZw4V3ROVUuq46i5cd5g&oe=62161B36&_nc_sid=83d603")
    bot.send_message(message.chat.id, "Satie Muradyan")
  
# newpassword 2.0
@bot.message_handler(commands = ["newpasswordultra"])
def newpassword_ultra_2(message):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+-=<>,.?/;:"

    string = lower + upper + numbers + symbols
    length = 16
    password = "".join(random.sample(string, length))
    bot.send_message(message.chat.id, "Your password is: " + password)

@bot.message_handler(commands = ["contact"])
def contact(message):
    bot.send_message(message.chat.id, "Telegram - @alexthegreatish \nFacebook - https://www.facebook.com/profile.php?id=100009196180783 \nGitHub - https://github.com/AAVVIronAlex \nInstagram - https://www.instagram.com/earthmapspictures/ \nReddit - https://www.reddit.com/user/AAVVIronAlex \nSpaceHey - https://spacehey.com/earthmapspictures \nTwitter - https://twitter.com/thealexgreater \nSpotify - https://open.spotify.com/user/1ygoezonte4i1hs73yj0qv0nb?si=dd1f41e818ba4cd5 \nYouTube - https://www.youtube.com/channel/UCcsUDEJ6HCUDSgT1gmEtxNQ/about \nMail - alex.babajanyan2015@gmail.com")

@bot.message_handler(commands = "mathexam")
def mathexam(message):
    today   = datetime.date.today()
    futdate = datetime.date(2022, 7, 15)
    now     = datetime.datetime.now()
    mnight  = now.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
    seconds = (mnight - now).seconds
    days    = (futdate - today).days
    hms     = str(datetime.timedelta(seconds = seconds))
    bot.send_message(message.chat.id, "Time remainiing until the exam is: %d days %s" % (days, hms))