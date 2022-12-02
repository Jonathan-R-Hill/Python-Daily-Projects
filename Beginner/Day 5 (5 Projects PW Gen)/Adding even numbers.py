nums = list(range(0, 101))
total = 0

for i in nums:
    if i % 2 == 0:
        total += i

print(f"The sum of all the even numbers is: {total}")