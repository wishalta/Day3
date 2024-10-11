import random

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
# yeap = pirmas[:3]                                  # taip gali paimti pirmas raides is string
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

# 6

# txt = 'An American in Paris'
# a = "Breakfast at Tiffany's"
# b = "2001: A Space Odyssey"
# c = "It's a Wonderful Life"
#
# print(txt.translate({ord(i): None for i in 'aAeEoOuUIi'}))      #kosmiska komanda translate, isgelbejo
# print(a.translate({ord(i): None for i in 'aAeEoOuUIi'}))
# print(b.translate({ord(i): None for i in 'aAeEoOuUIi'}))
# print(c.translate({ord(i): None for i in 'aAeEoOuUIi'}))

# 7

starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"

print(starWars)
