from emp import bot
import random
import string

@bot.message_handler(func=lambda message: True)
def echo_message(message):
  cid = message.chat.id
  mid = message.message_id 
  message_text = message.text 
  user_id = message.from_user.id 
  user_name = message.from_user.first_name 