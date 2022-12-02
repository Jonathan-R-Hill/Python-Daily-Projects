from random import randint, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters= int(input("How many letters would you like in your password?\n")) 
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

pw = []

for _ in range(num_letters):
    num = randint(0, len(letters) - 1)
    pw.append(letters[num])

for _ in range(num_symbols):
    num = randint(0, len(symbols) - 1)
    pw.append(symbols[num])

for _ in range(num_numbers):
    num = randint(0, len(numbers) - 1)
    pw.append(numbers[num])

shuffle(pw)

ans = ''.join(pw)

print(f"Your password is: \n{ans}")