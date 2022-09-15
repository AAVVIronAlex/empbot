from emp import bot
import random
import string

def reply(update, content):
    user_input = update.message.text
    update.message.reply_text(f"The text you have entered {user_input}")