# Exercise 6-5
major_rivers = {
    'nile': 'egypt',
    'amazon': 'peru',
    'mississippi': 'united states'
}

for river, country in major_rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

for river in major_rivers.keys():
    print(river.title())

for country in major_rivers.values():
    print(country.title())