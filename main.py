import random
import secrets

# 1

# pirmas = input('Jusu mylimo aktoriaus vardas: ')
# # antras = input('Jusu mylimo aktoriaus pavarde: ')
# #
# # if len(pirmas) < len(antras):            # len skaiciuoja ilgi
# #     print(f'{pirmas}')
# # else:
# #     print(f'{antras}')

# 2

# pirmas = input('Jusu mylimo aktoriaus vardas: ')
# antras = input('Jusu mylimo aktoriaus pavarde: ')
#
# txt = pirmas.upper()                              # upper viskas ddideliom
# tzt = antras.lower()                              # lower viskas mazom
#
# print(f'{txt} {tzt}')

# 3

# pirmas = input('Jusu mylimo aktoriaus vardas: ')
# antras = input('Jusu mylimo aktoriaus pavarde: ')
#
# yeap = pirmas[0:3]                                  # taip gali paimti pirmas raides is string
# yeah = antras[:3]
# print(f'{yeap} {yeah}')

# 4

# pirmas = input('Jusu mylimo aktoriaus vardas: ')
# antras = input('Jusu mylimo aktoriaus pavarde: ')
#
# txt = pirmas[-3:]                                  # taip gali paimti paskutines raides is string
# tzt = antras[-3:]
# print(f'{txt} {tzt}')

# 5

# txt = "An American in Paris"
# txt = txt.replace('A', '*' )            # taip galima pakeisti vieno type character i nauja
# txt = txt.replace('a', '*' )
# print(txt)

# txt = txt.replace('A', '*').replace('a', '*' )  # truumpesnis budas

# 6

# txt = 'An American in Paris'
# a = "Breakfast at Tiffany's"
# b = "2001: A Space Odyssey"
# c = "It's a Wonderful Life"
#
# print(txt.translate({ord(i): None for i in 'aAeEoOuUIiy'}))      #kosmiska komanda translate, isgelbejo
# print(a.translate({ord(i): None for i in 'aAeEoOuUIiy'}))
# print(b.translate({ord(i): None for i in 'aAeEoOuUIiy'}))
# print(c.translate({ord(i): None for i in 'aAeEoOuUIiy'}))
#
# # 7
#
# starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
#
# print(starWars)
#
# print(starWars.translate({ord(i): None for i in 'AaĄąBbCcČčDdEeĘęĖėFfGgHhIiĮįYyJjKkLlMmNnOoPpRrSsŠšTtUuŲųŪūVvZzŽžwW- :'}))

# 8 #10

text = "Don't Be a Menace to South Central While Drinking Your Juice in the Hood"
words = text.split()
count = 0
for word in words:
    if len(word) <= 5:
        count = count + 1

print(count)

txt = "Tik nereikia gąsdinti Pietų Centro, geriant sultis pas save kvartale"
wordss = txt.split()
count1 = 0
for wordd in wordss:
    if len(wordd) <= 5:
        count1 = count1 + 1
print(count1)

def Convert(string):
    li = list(string.split("f"))
    return li
print(Convert(text))
print(Convert(txt))
for  x in text:
    print(random.choice(text))

# listai, ciklai, salyginiai sakyniai
# 9

# from sys import stdout
# from random import choice
# from string import ascii_lowercase
#
# for _ in range(3):
#     stdout.write(choice(ascii_lowercase))

# 10


#
# def Convert(text):
#     li = list(text.split(" "))
#     return li
#
# gg = print(Convert(text,))
#
# gh = print(Convert(txt,))
#
# print(random.choice(gg))