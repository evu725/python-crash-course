# Exercise 6-11
cities = {
    'Boston': {
        'country': 'Barcelona',
        'population': '47,600,000',
        'fact': 'Spain is known for its rich cultural heritage and traditions, one of which is the world-famous "La Tomatina" festival.',

    },

    'Tokyo': {
        'country': 'Japan',
        'population': '13,960,236',
        'fact': 'Japan is known for its technological advancements and has the third-largest economy in the world.',
    },

    'New York City': {
        'country': 'United States',
        'population': '8,336,817',
        'fact': 'The United States is known for its cultural diversity and is often called a melting pot.',
    }
}

for city, info in cities.items():
    print(f"City: {city}")
    for key, value in info.items():
        print(f"{key.capitalize()}: {value}")
    print()