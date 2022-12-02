row1 = ["x", "x", "x"]
row2 = ["x", "x", "x"]
row3 = ["x", "x", "x"]

nested = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put your treasure? Enter as numbers as: col row\n")

ans = position.split(" ")

for i in range(len(ans)):
    ans[i] = int(ans[i])


nested[ans[0] - 1][ans[1] - 1] = "O"

for i in nested:
    print(f"{i}")
