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

boys = [
"Զուռնաչյան Տիգրան",
"Թևոսյան Դավիթ",
"Յավրյան Նարեկ",
"Սարգսյան Վահագն",
"Գրիգորյան Արմեն",
"Ջրաղացպանյան Պարգև",
"Դիլբարյան Նարեկ",
"Կոստանյան Շանթ",
"Մանուկյան Վրեժ",
"Մուքանյան Արսեն",
"Ջրաղացպանյան Վահե",
"Փամբուխչյան Անդրանիկ",
"Արաբյան Նարեկ Սերոփ",
"Բաբաջանյան Ալեքսանդր",
"Գազանճեան Ճոնի",
"Գևորգյան Դավիթ",
"Զաքարյան Գեղամ",
"Իսքանտար Պապա Նարեկ",
"Մկրտիչեան Վարագ",
"Սոլոյան Ալբերտ",
"Գազանճյան Տիգրան",
"Նազարյան Գոռ",
"Շահբազյան Ալբերտ",
"Սողոյան Արեն",
"Ավետիսյան Արեգ",
"Գևորգյան Վանիկ",
"Ենգիբարյան Վարդան",
"Զալինյան Տիգրան",
"Խաչատրյան Հայկ",
"Մելիքյան Վարդան",
"Տեր-Մաթևոսյան Տիգրան",
"Ղուկասյան Սպարտակ",
]

# Add if this if that in Version 2.8+

@bot.message_handler(commands = ["girlsrating"])
def girlsrating(message):
  bot.send_message(message.chat.id, "This is a program made to make it easier to choose a girl to dance with. \n For boy users enter /boysrating to take you to the boy randomiser menu. \n Commands: /givemeagirl \n And if you are confident that your score matches the girl you want try \n /ratedgirl<score> score = [0, 1, 2, 3, 4, 5]. \n More accurate scores will come with the 3rd update.")

@bot.message_handler(commands = ["boysrating"])
def boysrating(message):
  bot.send_message(message.chat.id, "This is a program made to make it easier to choose a boy to dance with. \n For boy users enter /girlsrating to take you to the girl randomiser menu. \n Commands: /givemeaboy. \n And if you are confident that your score matches the boy you want try \n /ratedboy<score> score = [0, 1, 2, 3, 4, 5]. \n More accurate scores will come with the 3rd update.")

boys_five_star = []
boys_four_star = []
boys_three_star = []
boys_two_star = []
boys_one_star = []

girls_five_star = ["Խանլարի Արինե", "Ավագյան Եվա", "Պետրոսյան Արփինե"]
girls_four_star = ["Տեր-Հարությունյան Սաթի", "Պետրոսյան Լյուդմիլա", "Գաբրիելյան Սյուզաննա", "Թամարյան Միլենա", "Ստեփանյան Հռիփսիմե", "Մանուկյան Մարինե", "Մախմուրյան Սիրանուշ"]
girls_three_star = ["Դավթյան Էլինա", "Վարդանյան Եվա", "Առաքելյան Իրեն", "Չիլինգարյան Անի", "Այվազյան Եվա", "Օհանյան Աննա", "Թադևոսյան Արփինե", "Գյոզալյան Տաթև", "Սիմոնյան Արփի", 
"Թորոսյան Անի", "Հայրիյան Էմիլյա", "Ղահրամանյան Ինգա"]
girls_two_star = ["Խոջաբագյան Ելենա", "Շերոյան Մագդալենա", "Մուրադյան Ամելի", "Օհանյան Թամարա", "Ավագյան Ռադհիկա", "Ամարյան Կարինա", "Բազեյան Եվա"]
girls_one_star = ["Այվազյան Ժաննա", "Թադևոսյան Ծովինար"]

# Rated girls

@bot.message_handler(commands = ["ratedgirl5"])
def rated_girl5(message):
  target = random.choice(girls_five_star)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["ratedgirl4"])
def rated_girl4(message):
  target = random.choice(girls_four_star)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["ratedgirl3"])
def rated_girl3(message):
  target = random.choice(girls_three_star)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["ratedgirl2"])
def rated_girl2(message):
  target = random.choice(girls_two_star)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["ratedgirl1"])
def rated_girl1(message):
  target = random.choice(girls_one_star)
  bot.send_message(message.chat.id, target)

# Rated boys

@bot.message_handler(commands = ["ratedboy5"])
def rated_boy5(message):
  target = random.choice(boys_five_star)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["ratedboy4"])
def rated_boy4(message):
  target = random.choice(boys_four_star)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["ratedboy3"])
def rated_boy3(message):
  target = random.choice(boys_three_star)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["ratedboy2"])
def rated_boy2(message):
  target = random.choice(boys_two_star)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["ratedboy1"])
def rated_boy1(message):
  target = random.choice(boys_one_star)
  bot.send_message(message.chat.id, target)

# Fully Random

@bot.message_handler(commands = ["givemeagirl"])
def givemeagirl(message):
  target = random.choice(girls)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["givemeaboy"])
def givemeaboy(message):
  target = random.choice(boys)
  bot.send_message(message.chat.id, target)