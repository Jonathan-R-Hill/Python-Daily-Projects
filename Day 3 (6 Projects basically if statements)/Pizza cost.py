size = input("What size Pizaz do you want? S, M or L\n").capitalize()
pepperoni = input("Would you like pepperoni adding to your Pizza? Y or N\nOn a S pizza it will cost $2. On a M or L it costs $3\n").capitalize()
cheese = input("Do you want extra cheese for an extra $1? Y or N\n").capitalize()

size_dict = {'S': 15.00,
             'M': 20.00,
             'L': 25.00
             }

def price(size):
    if size in size_dict:
        price = size_dict[size]
    
    else:
        price = "That is not a valid size"
    return price

price = price(size)

if pepperoni == 'Y':
    if size == 'S':
        price += 2
    
    if size == 'M' or size == 'L':
        price += 3

if cheese == 'Y':
    price += 1

print(f"Your total cost is ${price}")

