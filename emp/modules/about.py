from emp import bot


@bot.message_handler(commands=["help"])
def hello(message):
    bot.send_message(message.chat.id, "If you type /hello I will say hello.")
    bot.send_message(message.chat.id, "If If you type /greet I will greet you.")
    bot.send_message(
        message.chat.id,
        "If you are a Waka Masters member type /waka for a surprise.",
    )
    bot.send_message(message.chat.id, "/about is about")
    bot.send_message(message.chat.id, "Also I like to make jokes.")
    bot.send_message(message.chat.id, "Upgrade to EMP Bot Premium to see this message.")
    bot.send_message(message.chat.id, "Upgrade to EMP Bot Premium to see this message.")
    bot.send_message(message.chat.id, "Answer?")
    bot.send_message(
        message.chat.id,
        "Oh yeah sorry. We dont have Premium its completely free to do anything"
        " with EMP Bot! That was a EA joke Pay to Play get it?",
    )


@bot.message_handler(commands=["emp"])
def emp(message):
    bot.send_message(message.chat.id, "earthmapspictures.weebly.com")


@bot.message_handler(commands=["about"])
def about(message):
    bot.send_message(
        message.chat.id, "Copyright EarthMapsPictures Inc. 2015-2022"
    )
    bot.send_message(message.chat.id, "Developed by @alexthegreatish and EarthMapsPictures Inc.")
