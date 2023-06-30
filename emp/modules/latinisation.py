from emp import bot
import random
import string

@bot.message_handler(commands = ["latinisation"])
def latinisation(message):
    bot.send_message(message.chat.id, "This function is not yet available on the @earthmapspicturesbot, go check out @wakamastersbot to use it.")