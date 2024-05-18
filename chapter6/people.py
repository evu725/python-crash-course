# Exercise 6-7
person1 = {'first_name': 'Asa', 
            'last_name': 'Mitaka', 
            'age': '17', 
            'city': 'Tokyo'}

person2 = {'first_name': 'Kobeni', 
            'last_name': 'Higashiyama', 
            'age': '20', 
            'city': 'Tokyo'}

person3 = {'first_name': 'Hirofumi', 
            'last_name': 'Yoshida', 
            'age': '18', 
            'city': 'Tokyo'}

people = [person1, person2, person3]

for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print("\n")