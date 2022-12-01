total_cost = float(input("Enter your total bill: "))
tip = float(input("Enter what percentage you would like to tip: "))

tipcost = total_cost * (tip / 100)

total = round(total_cost + tipcost , 2)

print(f"Your new total including the tip is: {total}")
