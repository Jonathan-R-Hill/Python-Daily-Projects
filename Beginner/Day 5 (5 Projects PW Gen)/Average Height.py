heights = [170, 200, 165, 152, 183, 176, 162, 158]
total = 0

lenheights = len(heights)

for i in range(lenheights):
    total += heights[i]

average = round(total / lenheights)

print(f"The total height is: {total}\nThe average height is {average}")