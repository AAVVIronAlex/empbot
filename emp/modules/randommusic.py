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
    "https://www.youtube.com/watch?v=Qyhbd_5JTJk",
    "https://www.youtube.com/watch?v=Nplz679dsEI",
    "https://www.youtube.com/watch?v=G_ql5IoVcro",
    "https://www.youtube.com/watch?v=GDZPkxBHvzA",
    "https://www.youtube.com/watch?v=jSL1nXza7pM",
    "https://www.youtube.com/watch?v=GHPWLL8EqGw",
    "https://www.youtube.com/watch?v=req-U0G5PCc",
    "https://www.youtube.com/watch?v=8wZTljHP5uA",
    "https://www.youtube.com/watch?v=N4Y81rkT_5o",
    "https://www.youtube.com/watch?v=VrQRPg050gI",
    "https://www.youtube.com/watch?v=rzRqEWJYwX4",
    "https://www.youtube.com/watch?v=GrBgOEMEqyE",
    "https://www.youtube.com/watch?v=zR_477WqAE4",
    "https://www.youtube.com/watch?v=TzLZN1K-PUE",
    "https://www.youtube.com/watch?v=CN-RcplEW5c",
    "https://www.youtube.com/watch?v=SEbxwmjScr8",
    "https://www.youtube.com/watch?v=JW5UEW2kYvc",
    "https://www.youtube.com/watch?v=_PLq0_7k1jk",
    "https://www.youtube.com/watch?v=QJX-nnCjoUM",
    "https://www.youtube.com/watch?v=iG8SmgtoZgM"
]

@bot.message_handler(commands = ["randommusic"])
def randommusic(message):
    target = random.choice(music)
    bot.send_message(message.chat.id, target)
