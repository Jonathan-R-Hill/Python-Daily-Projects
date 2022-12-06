from Cdata import MENU, resources

# TODO  take away resources upon payment success 

print(resources)

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]


def requiredresources(drink):
    drink_indict = MENU[drink]

    water_req = drink_indict["ingredients"]["water"]
    milk_req = drink_indict["ingredients"]["milk"]
    coffee_req = drink_indict["ingredients"]["coffee"]
    price = drink_indict["cost"]

    if water >= water_req:
        if milk >= milk_req:
            if coffee >= coffee_req:
                return water_req, milk_req, coffee_req, price

    else:
        price = "Insufficient resources"
        return water_req, milk_req, coffee_req, price


def payment():
    coins = []
    fives = int(input("How many 5 Pences will you pay with?   "))
    tens = int(input("How many 10 Pences will you pay with?   "))
    twenties = int(input("How many 20 Pences will you pay with?   "))
    fifties = int(input("How many 50 Pences will you pay with?   "))

    coins.append((fives * 5) / 100)
    coins.append((tens * 10) / 100)
    coins.append((twenties * 20) / 100)
    coins.append((fifties * 50) / 100)
    total = sum(coins)

    return total


def take_away():
    global water
    global milk
    global coffee

    value = []
    for i in requiredresources(drink=what_drink):
        value.append(i)

    water -= value[0]
    milk -= value[1]
    coffee -= value[2]


while True:
    what_drink = input("What drink would you like?\nespresso\nlatte\ncappuccino\n").lower()

    if what_drink == "report":
        cost = 0
    elif what_drink == "off":
        cost = "off"
    else:
        cost = requiredresources(drink=what_drink)[3]

    if cost == "Insufficient resources" or cost == "off":
        print(cost)
        break

    if cost == 0:
        print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}")

    else:
        print(cost)
        pay = payment()
        if pay >= cost:
            print(f"Here's your {what_drink}. Your change is: {pay - cost}")
            take_away()
        else:
            print("You did not provide sufficient payment. Required {cost}. Your payment: {pay}")
