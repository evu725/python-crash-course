# Exercise 5-10
current_users = ['classypax', 'jennybear', 'blau', 'carmen', 'thechief1114']
new_users = ['katie', 'crystalst', 'jennybear', 'aicandii', 'carmen']

for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} username is not available, please enter new username")
    else:
        print(f"{new_user} username is avaliable.")