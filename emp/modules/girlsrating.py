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

# Getting ready for version 3.0

_50_girls = []
_49_girls = ["Խանլարի Արինե", "Ավագյան Եվա"]
_48_girls = []
_47_girls = []
_46_girls = ["Պետրոսյան Արփինե"]
_45_girls = []
_44_girls = ["Մախմուրյան Սիրանուշ"]
_43_girls = []
_42_girls = []
_41_girls = []
_40_girls = []
_39_girls = ["Ստեփանյան Հռիփսիմե"]
_38_girls = ["Թամարյան Միլենա"]
_37_girls = ["Պետրոսյան Լյուդմիլա", "Մանուկյան Մարինե"]
_36_girls = ["Տեր-Հարությունյան Սաթի"]
_35_girls = ["Գաբրիելյան Սյուզաննա"]
_34_girls = ["Դավթյան Էլինա", "Չիլինգարյան Անի", "Հայրիյան Էմիլյա"]
_33_girls = ["Վարդանյան Եվա", "Այվազյան Եվա"]
_32_girls = ["Օհանյան Աննա"]
_31_girls = ["Թադևոսյան Արփինե", "Գյոզալյան Տաթև"]
_30_girls = []
_29_girls = ["Առաքելյան Իրեն"]
_28_girls = ["Թորոսյան Անի"]
_27_girls = ["Ղահրամանյան Ինգա"]
_26_girls = ["Սիմոնյան Արփի"]
_25_girls = []
_24_girls = ["Խոջաբագյան Ելենա"]
_23_girls = ["Շերոյան Մագդալենա"]
_22_girls = ["Օհանյան Թամարա"]
_21_girls = ["Բազեյան Եվա"]
_20_girls = ["Ավագյան Ռադհիկա"]
_19_girls = []
_18_girls = ["Ամարյան Կարինա"]
_17_girls = []
_16_girls = []
_15_girls = ["Մուրադյան Ամելի"]
_14_girls = []
_13_girls = []
_12_girls = ["Թադևոսյան Ծովինար"]
_11_girls = []
_10_girls = ["Այվազյան Ժաննա"]
_09_girls = []
_08_girls = []
_07_girls = []
_06_girls = []
_05_girls = []

_50_boys = ["Still working on it..."]
_49_boys = ["Still working on it..."]
_48_boys = ["Still working on it..."]
_47_boys = ["Still working on it..."]
_46_boys = ["Still working on it..."]
_45_boys = ["Still working on it..."]
_44_boys = ["Still working on it..."]
_43_boys = ["Still working on it..."]
_42_boys = ["Still working on it..."]
_41_boys = ["Still working on it..."]
_40_boys = ["Still working on it..."]
_39_boys = ["Still working on it..."]
_38_boys = ["Still working on it..."]
_37_boys = ["Still working on it..."]
_36_boys = ["Still working on it..."]
_35_boys = ["Still working on it..."]
_34_boys = ["Still working on it..."]
_33_boys = ["Still working on it..."]
_32_boys = ["Still working on it..."]
_31_boys = ["Still working on it..."]
_30_boys = ["Still working on it..."]
_29_boys = ["Still working on it..."]
_28_boys = ["Still working on it..."]
_27_boys = ["Still working on it..."]
_26_boys = ["Still working on it..."]
_25_boys = ["Still working on it..."]
_24_boys = ["Still working on it..."]
_23_boys = ["Still working on it..."]
_22_boys = ["Still working on it..."]
_21_boys = ["Still working on it..."]
_20_boys = ["Still working on it..."]
_19_boys = ["Still working on it..."]
_18_boys = ["Still working on it..."]
_17_boys = ["Still working on it..."]
_16_boys = ["Still working on it..."]
_15_boys = ["Still working on it..."]
_14_boys = ["Still working on it..."]
_13_boys = ["Still working on it..."]
_12_boys = ["Still working on it..."]
_11_boys = ["Still working on it..."]
_10_boys = ["Still working on it..."]
_09_boys = ["Still working on it..."]
_08_boys = ["Still working on it..."]
_07_boys = ["Still working on it..."]
_06_boys = ["Still working on it..."]
_05_boys = ["Still working on it..."]

# Get ready for version 4.0

boys_five_star = []
boys_four_star = []
boys_three_star = []
boys_two_star = []
boys_one_star = []

girls_five_star = ["Խանլարի Արինե", "Ավագյան Եվա", "Պետրոսյան Արփինե"]
girls_four_star = ["Տեր-Հարությունյան Սաթի", "Պետրոսյան Լյուդմիլա", "Գաբրիելյան Սյուզաննա", "Թամարյան Միլենա", "Ստեփանյան Հռիփսիմե", "Մանուկյան Մարինե", "Մախմուրյան Սիրանուշ"]
girls_three_star = ["Դավթյան Էլինա", "Վարդանյան Եվա", "Առաքելյան Իրեն", "Չիլինգարյան Անի", "Այվազյան Եվա", "Օհանյան Աննա", "Թադևոսյան Արփինե", "Գյոզալյան Տաթև", "Սիմոնյան Արփի", "Թորոսյան Անի", "Հայրիյան Էմիլյա", "Ղահրամանյան Ինգա"]
girls_two_star = ["Խոջաբագյան Ելենա", "Շերոյան Մագդալենա", "Մուրադյան Ամելի", "Օհանյան Թամարա", "Ավագյան Ռադհիկա", "Ամարյան Կարինա", "Բազեյան Եվա"]
girls_one_star = ["Այվազյան Ժաննա", "Թադևոսյան Ծովինար"]

# Next gen rated girls (Version 3.x)

@bot.message_handler(commands = ["targetgirl5"])
def target_girl5(message):
  chance = [14, 14, 14, 14, 14, 14, 14, 1, 1]
  girls_5 = [_50_girls, _49_girls, _48_girls, _47_girls, _46_girls, _45_girls, "Ավագյան Եվա", girls_four_star, girls_three_star]
  target = random.choices(girls_5, chance, k = 1000)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["targetgirl4"])
def target_girl4(message):
  chance = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5, 5]
  girls_3 = [_44_girls, _43_girls, _42_girls, _41_girls, _40_girls, _39_girls, _38_girls, _37_girls, _36_girls, _35_girls, girls_five_star, girls_three_star]
  target = random.choices(girls_3, chance, k = 100)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["targetgirl3"])
def target_girl3(message):
  chance = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5, 5]
  girls_3 = [_34_girls, _33_girls, _32_girls, _31_girls, _30_girls, _29_girls, _28_girls, _27_girls, _26_girls, _25_girls, girls_four_star, girls_three_star]
  target = random.choices(girls_3, chance, k = 100)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["targetgirl2"])
def target_girl2(message):
  chance = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5, 5]
  girls_2 = [_24_girls, _23_girls, _22_girls, _21_girls, _20_girls, _19_girls, _18_girls, _17_girls, _16_girls, _15_girls, girls_three_star, girls_one_star]
  target = random.choices(girls_2, chance, k = 100)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["targetgirl1"])
def target_girl1(message):
  chance = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5, 5]
  girls_1 = [_14_girls, _13_girls, _12_girls, _11_girls, _10_girls, _09_girls, _08_girls, _07_girls, _06_girls, _05_girls, girls_two_star, girls_three_star]
  target = random.choices(girls_1, chance, k = 100)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["targetboy5"])
def target_boy5(message):
  chance = [14, 14, 14, 14, 14, 14, 14, 1, 1]
  boys_5 = [_50_boys, _49_boys, _48_boys, _47_boys, _46_boys, _45_boys, boys_two_star, boys_four_star, boys_three_star]
  target = random.choices(boys_5, chance, k = 100)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["targetboy4"])
def target_boy4(message):
  chance = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5, 5]
  boys_3 = [_44_boys, _43_boys, _42_boys, _41_boys, _40_boys, _39_boys, _38_boys, _37_boys, _36_boys, _35_boys, boys_five_star, boys_three_star]
  target = random.choices(boys_3, chance, k = 100)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["targetboy3"])
def target_boy3(message):
  chance = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5, 5]
  boys_3 = [_34_boys, _33_boys, _32_boys, _31_boys, _30_boys, _29_boys, _28_boys, _27_boys, _26_boys, _25_boys, boys_four_star, boys_three_star]
  target = random.choices(boys_3, chance, k = 100)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["targetboy2"])
def target_boy2(message):
  chance = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5, 5]
  boys_2 = [_24_boys, _23_boys, _22_boys, _21_boys, _20_boys, _19_boys, _18_boys, _17_boys, _16_boys, _15_boys, boys_three_star, boys_one_star]
  target = random.choices(boys_2, chance, k = 100)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["targetboy1"])
def target_boy1(message):
  chance = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 5, 5]
  boys_1 = [_14_boys, _13_boys, _12_boys, _11_boys, _10_boys, _09_boys, _08_boys, _07_boys, _06_boys, _05_boys, boys_two_star, boys_three_star]
  target = random.choices(boys_1, chance, k = 100)
  bot.send_message(message.chat.id, target)

# Rated girls (Version 2.x)

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

# Rated boys (Version 2.x)

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

# Fully Random (Version 1.x)

@bot.message_handler(commands = ["givemeagirl"])
def givemeagirl(message):
  target = random.choice(girls)
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["givemeaboy"])
def givemeaboy(message):
  target = random.choice(boys)
  bot.send_message(message.chat.id, target)

#Cheat codes

@bot.message_handler(commands = ["pleaseme"])
def pleaseme(message):
  target = ["Խանլարի Արինե"]
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["disappointme"])
def disappointme(message):
  target = ["Առաքելյան Իրեն"]
  bot.send_message(message.chat.id, target)

@bot.message_handler(commands = ["givemeaverage"])
def disappointme(message):
  averages = ["Գաբրիելյան Սյուզաննա",
  "Ստեփանյան Հռիփսիմե",
  "Դավթյան Էլինա", "Վարդանյան Եվա",
  "Առաքելյան Իրեն",
  "Չիլինգարյան Անի",
  "Այվազյան Եվա",
  "Օհանյան Աննա",
  "Թադևոսյան Արփինե",
  "Գյոզալյան Տաթև", 
  "Սիմոնյան Արփի", 
  "Թորոսյան Անի", 
  "Հայրիյան Էմիլյա", 
  "Մուրադյան Ամելի", 
  "Օհանյան Թամարա", 
  "Ավագյան Ռադհիկա", 
  "Ամարյան Կարինա"]
  target = random.choice(averages)
  bot.send_message(message.chat.id, target)