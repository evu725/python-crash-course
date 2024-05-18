# Exercise 6-9
favorite_places = {
    'kathy': ['beach'],
    'Lia': ['park', 'beach'],
    'Janise': ['mountains']
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite place are: ") 
    for place in places:
        print(f"\t{place.title()}")
    print("\n")