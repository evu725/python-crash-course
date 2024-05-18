# Exercise 6-2
favorite_number = {
    'fingle dan': '1114',
    'dingle dan': '7',
    'wingle dan': '89',
    'vingle dan': '13',
    'peachingle dan': '2'
}
print(favorite_number)

favorite_number = {
    'fingle dan': ['1114'],
    'dingle dan': ['7', '222'],
    'wingle dan': ['89', '2'],
    'vingle dan': ['13, 1114', '2'],
    'peachingle dan': ['2']
}

# Exercise 6-10
for name, numbers in favorite_number.items():
    print(f"{name.title()}'s favorite number are: ") 
    for number in numbers:
        print(f"\t{number}")
    print("\n")