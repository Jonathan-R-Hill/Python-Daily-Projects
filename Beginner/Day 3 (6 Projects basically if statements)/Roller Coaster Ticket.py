height = int(input("Enter your height in CM:  "))
age = int(input("Enter your age:  "))


def height_age(height, age):
    
    if age < 12 or height < 120:
        ticket_price = ("You cannot go on this ride.")
        
    if height > 120 and age > 12:
        
        if age > 12 and age < 18:
            ticket_price = 5.00
        
        elif age > 18 and age < 40:
            ticket_price = 7.00
            
        else:
            ticket_price = 6.00
    
    return ticket_price

price = height_age(height, age)

if price != "You cannot go on this ride.":
    
    print(f"Your ticket will cost: ${price}")
    photo = input("Would you like a photo with your ticket for $3? Y or N\n").capitalize()
    
    if photo == 'Y':
        price += 3
        
    print(f"Your total cost come to: ${price}")
