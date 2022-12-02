scores = [11, 90, 88, 61, 41, 91, 10, 77, 22]
scores.sort()
total = 0

for i in scores:
    total += i

average = round(total / len(scores))

print(f'The biggest number is: {scores[-1]}')
print(f'The smallest number is: {scores[0]}')
print(f'The average is: {average}')