# Exercise 6-4
glossary = {'list': 'collection of items in a particular order', 
                     'tuple': 'immuntable list', 
                     'dictionary': 'collection of key-values pairs', 
                     'boolean value': 'either True or False',
                     'multiple assignment': 'assign values to more than one variable'}

for key, value in glossary.items():
    print(f"{key} means {value}")