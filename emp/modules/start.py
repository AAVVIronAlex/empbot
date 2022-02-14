from emp import bot

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Hello I am EarthMapsPictures Bot. The Official EarthMapsPictures Website:"
        " https://earthmapspictures.weebly.com/",
    )
    bot.send_message(message.chat.id, "Type /help to see what I can do!")

@bot.message_handler(commands=["greet"])
def greet(message):
    bot.reply_to(message, "Hey! What up?")

@bot.message_handler(commands=["hello"])
def hello(message):
    bot.send_message(message.chat.id, "Hello!")
