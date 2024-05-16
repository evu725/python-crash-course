# Exercise 3-8
guest = ["Rose", "Lisa", "Jennie"]
print(guest[2])
guest[2] = "Jisoo"
print("Hi, " + guest[0] + " we would like to invite you to dinner.")
print("Hi, " + guest[1] + " we would like to invite you to dinner.")
print("Hi, " + guest[2] + " we would like to invite you to dinner.")
print("\n")
print("Hi everyone, we have decided to bring three more guests to dinner")
# add in beginning of list
guest.insert(0, "Irene")
# add in middle of the list
guest.insert(2, "Nayeon")
# add in end of list
guest.append("Mina")

print("Hi, " + guest[0] + " we would like to invite you to dinner.")
print("Hi, " + guest[1] + " we would like to invite you to dinner.")
print("Hi, " + guest[2] + " we would like to invite you to dinner.")
print("Hi, " + guest[3] + " we would like to invite you to dinner.")
print("Hi, " + guest[4] + " we would like to invite you to dinner.")
print("Hi, " + guest[5] + " we would like to invite you to dinner.")

print("Hello everyone, due to some circumstances I can only invite two people for dinner")
print(guest.pop(), "Hello, I'm sorry I can't invite you to dinner")
print(guest.pop(), "Hello, I'm sorry I can't invite you to dinner")
print(guest.pop(), "Hello, I'm sorry I can't invite you to dinner")
print(guest.pop(), "Hello, I'm sorry I can't invite you to dinner")

print(guest[0], "you're still invited to dinner")
print(guest[1], "you're still invited to dinner")
del guest[0]
del guest[0]
print(guest)
