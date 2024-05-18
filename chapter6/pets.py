# Exercise 6-8
pet1 = {'animal': 'rabbit', 
        'owner': 'Asa', 
        }

pet2 = {'animal': 'dog', 
        'owner': 'Denji', 
        }

pet3 = {'animal': 'bird', 
        'owner': 'Kobeni', 
        }

pets = [pet1, pet2, pet3]

for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print("\n")