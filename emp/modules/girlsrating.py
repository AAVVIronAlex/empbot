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
"Զալինյան Տիգրան",
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

#print("Your target f=girl is:", target)

@bot.message_handler(commands=["givemeagirl"])
def givemeagirl(message):
  target = random.choice(girls)
  bot.send_message(message.chat.id, target)