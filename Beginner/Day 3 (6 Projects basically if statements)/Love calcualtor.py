print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

check = "truelove"
total1 = 0
total2 = 0


for let in name1:
    if let in check:
        total1 += 1

for let in name2:
    if let in check:
        total2 += 1

total = (str(total1) + str(total2))

if int(total) < 10 or int(total) > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")

elif int(total) >= 50 or int(total) <= 60:
    print(f"Your score is {total}, you are alright together.")

else:
    print(f"Your score is {total}.")