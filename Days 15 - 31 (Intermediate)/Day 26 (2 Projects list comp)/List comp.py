# [new_item for item in list if test]

numbers = list(range(1, 100))
add = [n+1 for n in numbers]
double = [num + num for num in range(1, 5)]
sqaures = [n*n for n in numbers]


name = "Jonathan"
letters = [letter for letter in name]

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
less4 = [name for name in names if len(name) <= 4]

uppercase5 = [name.upper() for name in names if len(name) >= 5]


