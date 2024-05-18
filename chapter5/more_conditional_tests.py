# Exercise 5-2
pokemon = 'pikachu'

# testing for equality and inequality
print(pokemon=='pikachu')
print(pokemon!='pikachu')
print("\n")

# testing lower method
pokemon = 'Pikachu'
print(pokemon.lower()== 'pikachu')
print("\n")

# numerical tests
number = 707
print(number > 202)
print(number < 12)
print(number != 707)
print(number == 707)
print("\n")

# and keyword and or keyword
print(number <707 and number > 42)
print(number < 749 or number > 42)
print("\n")

# item is in list and item not in list
pokemon = ["tinkaton", 'rowlet', 'mudkip', 'munchlax']
print('munchlax' in pokemon)
print('eevee' not in pokemon)