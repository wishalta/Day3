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

txt = 'An American in Paris'
a = "Breakfast at Tiffany's"
b = "2001: A Space Odyssey"
c = "It's a Wonderful Life"

print(txt.translate({ord(i): None for i in 'aAeEoOuUIiy'}))      #kosmiska komanda translate, isgelbejo
print(a.translate({ord(i): None for i in 'aAeEoOuUIiy'}))
print(b.translate({ord(i): None for i in 'aAeEoOuUIiy'}))
print(c.translate({ord(i): None for i in 'aAeEoOuUIiy'}))

# 7

starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"

print(starWars)

print(starWars.translate({ord(i): None for i in 'AaĄąBbCcČčDdEeĘęĖėFfGgHhIiĮįYyJjKkLlMmNnOoPpRrSsŠšTtUuŲųŪūVvZzŽžwW- :'}))

# 8

# string = "Don't Be a Menace to South Central While Drinking Your Juice in the Hood"
#
# s = len(string.split())
# print(s)



# text = "Don't Be a Menace to South Central While Drinking Your Juice in the Hood"
# text = split()
# def greater_5(text):
# 	letters = [1 for word in text if len(word)>5]
#
# 	return sum(letters)
#
# print(greater_5(text))