from random import randint

get = input("Pick one: Heads or Tails:  ").lower()

options = ["heads", "tails", "heads", "tails"]

ans = options[randint(0, 3)]

if get == ans:
    print(f"You won! You chose: {get} and the coin flipped: {ans}")

else:
    print(f"You lost! You chose: {get} and the coin flipped: {ans}")