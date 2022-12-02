from random import randint

people = input("Enter the names of the people involved separated by commas:\n")

ppl = people.split(',')

range = len(ppl)

ans = ppl[randint(0, range)]

print(f"{ans} will pay this time!")