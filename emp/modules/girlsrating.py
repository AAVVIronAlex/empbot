from emp import bot
import random
import string

girls = ["Ավագյան Նարե",
"Դավթյան Էլինա",
"Երիցյան Էմիլյա",
"Թադևոսյան Արփինե",
"Թամարյան Միլենա",
"Խանլարի Արինե",
"Խոջաբագյան Ելենա",
"Վարդանյան Եվա",
"Ամարյան Կարինա",
"Այվազյան Ժաննա",
"Գրիգորյան Նունե",
"Հակոբյան Վալերիա",
"Համբարձումյան Սելվի",
"Ղահրամանյան Ինգա",
"Մոսիկյան Նանե",
"Ստեփանյան Հռիփսիմե",
"Քոշկարյան Մանե",
"Գյոզալյան Տաթև",
"Ղասումյան Սյուզի",
"Մանուկյան Մարինե",
"Միրզոյան Էլինա",
"Մկրտչյան Աննա",
"Չիլինգարյան Անի",
"Պետրոսյան Լյուդմիլա",
"Սիմոնյան Արփի",
"Օհանյան Աննա",
"Առաքելյան Իրեն",
"Բազդասարյան Մարիամ",
"Թորոսյան Անի",
"Մախմուրյան Սիրանուշ",
"Շերոյան Մագդալենա",
"Տեր-Հարությունյան Սաթի",
"Ավագյան Եվա",
"Բազեյան Եվա",
"Գաբրիելյան Սյուզաննա",
"Դավեյան Գոհար",
"Հայրիյան Էմիլյա",
"Չերքեզյան Ասթինե",
"Պետրոսյան Աննա",
"Պետրոսյան Արփինե",
"Ստեփանյան Սոնա",
"Օհանյան Թամարա",
"Ադամյան Մարիէտտա",
"Այվազյան Եվա",
"Ավագյան Ռադհիկա",
"Թադևոսյան Ծովինար",
"Համբարձումյան Մերի",
"Մուրադյան Ամելի",
"Շահրամանյան Աննա",
"Քուրթյան Ռոզի",
"Սևիկյան Սոնա",
"Աթալյան Էլեն",
"Բաբայան Աննա",
"Հայրապետյան Մարիամ",
"Գրիգորյան Լիա"]

five_star = ["Խանլարի Արինե", "Թադևոսյան Արփինե", "Ավագյան Եվա"]
four_star = ["Տեր-Հարությունյան Սաթի", "Պետրոսյան Լյուդմիլա", "Գաբրիելյան Սյուզաննա", "Թամարյան Միլենա", "Ստեփանյան Հռիփսիմե", "Մանուկյան Մարինե", "Մախմուրյան Սիրանուշ"]
three_star = ["Դավթյան Էլինա", "Վարդանյան Եվա", "Առաքելյան Իրեն", "Չիլինգարյան Անի", "Այվազյան Եվա", "Օհանյան Աննա", "Պետրոսյան Արփինե", "Գյոզալյան Տաթև", "Սիմոնյան Արփի", 
"Թորոսյան Անի", "Հայրիյան Էմիլյա"]
two_star = ["Խոջաբագյան Ելենա", "Շերոյան Մագդալենա", "Մուրադյան Ամելի", "Օհանյան Թամարա", "Ավագյան Ռադհիկա", "Ամարյան Կարինա", "Բազեյան Եվա"]
one_star = ["Այվազյան Ժաննա", "Թադևոսյան Ծովինար"]
zero_star = ["Ղահրամանյան Ինգա"]

@bot.message_handler(commands = ["ratedgirl5"])
def rated_girl5(message):
  target = random.choice(five_star)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["ratedgirl4"])
def rated_girl4(message):
  target = random.choice(four_star)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["ratedgirl3"])
def rated_girl3(message):
  target = random.choice(three_star)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["ratedgirl2"])
def rated_girl2(message):
  target = random.choice(two_star)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["ratedgirl1"])
def rated_girl1(message):
  target = random.choice(one_star)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["ratedgirl0"])
def rated_girl0(message):
  target = random.choice(zero_star)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["givemeagirl"])
def givemeagirl(message):
  target = random.choice(girls)
  bot.send_message(message.chat.id, target)
