# Exercise 6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

list = ['sarah', 'eri', 'nash', 'jen',]
for name in list:
    if name in favorite_languages.keys():
        print(f"Thank you {name} for responding!")
    else:
        print(f"{name}, please take the poll when you get the chance.")