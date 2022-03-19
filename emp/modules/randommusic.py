from emp import bot
import random
import string

music = [
    "https://www.youtube.com/watch?v=w0m0hTrtlWM&t=28s",
    "https://www.youtube.com/watch?v=QK-Z1K67uaA",
    "https://www.youtube.com/watch?v=SUzsih7QJSY",
    "https://www.youtube.com/watch?v=qqK1FrO3BdM",
    "https://www.youtube.com/watch?v=s6WGNd8QR-U",
    "https://www.youtube.com/watch?v=-50cU8DqJzs",
    "https://www.youtube.com/watch?v=F82nyLAAUrk",
    "https://www.youtube.com/watch?v=qqK1FrO3BdM",
    "https://youtu.be/XoJ6TPUG1Tk",
    "https://www.youtube.com/watch?v=AKHSWvmiwP8",
    "https://www.youtube.com/watch?v=c8qrwON1-zE",
    "https://www.youtube.com/watch?v=DJaPakxf2fQ",
    "https://www.youtube.com/watch?v=Qyhbd_5JTJk"
]

@bot.message_handler(commands = ["randommusic"])
def randommusic(message):
    target = random.choice(music)
    bot.send_message(message.chat.id, target)
