# Exercise 5-8
usernames = ['admin', 'jennybear', 'blau', 'mekabear', 'thechief1114']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for loggin in again.")