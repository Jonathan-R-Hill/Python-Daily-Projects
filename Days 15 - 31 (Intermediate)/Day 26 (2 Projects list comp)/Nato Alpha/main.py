import pandas as pd

file = "nato_alpha.csv"
df = pd.DataFrame(pd.read_csv(file))

nato = {row.letter:row.code for index, row in df.iterrows()}

name = input("Enter your name:  ")

nato_name = [nato[let] for let in name.upper()]

print(nato_name)

