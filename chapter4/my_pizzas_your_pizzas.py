# Exercise 4-11
my_pizzas = ["Chicago", "New York", "Detroit", "Californian", "Italian"]

# Copy orignial list to new list
friend_pizzas = my_pizzas[:]
friend_pizzas.append("Boston")

print("My favorite pizzas are: ")
for values in my_pizzas:
    print(values)
print("\n")

print("My friend's favorite pizzas are: ")
for values in friend_pizzas:
    print(values)