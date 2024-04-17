import random

Alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Symbols = ['!', '#', '@', '$', '%', '&', '(', ')', '*', '+']



nr_letters = int(input("Please confirm the number of letters : "))
nr_numbers = int(input("Please confirm the number of numbers : "))
nr_symbols = int(input("Please confirm the number of symbols : "))

password =[]

for char in range(1, nr_letters+1):
    password += random.choice(Alphabets)

for char in range(1, nr_numbers+1):
    password += random.choice(Numbers)

for char in range(1, nr_symbols+1):
    password += random.choice(Symbols)

random.shuffle(password)

for i in password:
    print(i, end="")


