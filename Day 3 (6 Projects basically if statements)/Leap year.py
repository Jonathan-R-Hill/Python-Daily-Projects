print("Leap year checker!")
year = int(input("What year do you want to check?\n"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("It's a leap year")

else:
    print("It is not a leap year")