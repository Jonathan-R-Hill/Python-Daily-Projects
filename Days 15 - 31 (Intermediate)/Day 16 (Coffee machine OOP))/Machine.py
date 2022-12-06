import prettytable

class Res_Data:
    def __init__(self):
        
        self.water = 500
        self.coffee = 400
        self.milk = 350
        
        self.money = 0
        self.drink_price = 0.00
        self.brew = ''
        
        self.Menu = {
            "espresso": {
                "ingredients": {
                    "water": 50,
                    "milk": 0,
                    "coffee": 18,
                },
                "cost": 1.5,
            },
            "latte": {
                "ingredients": {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
                "cost": 2.5,
            },
            "cappuccino": {
                "ingredients": {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
                "cost": 3.0,
            }
        }
    
    
    def report(self):
        table = prettytable.PrettyTable()
        table.field_names = ["Rescource", "Amount"]
        table.add_row(["water", self.water])
        table.add_row(["coffee", self.coffee])
        table.add_row(["milk", self.milk])
        table.add_row(["Money", self.money])
        
        print(table)
    
    
    def reduce(self):
        self.water -= self.Menu[self.brew]["ingredients"]["water"]
        self.coffee -= self.Menu[self.brew]["ingredients"]["coffee"]
        self.milk -= self.Menu[self.brew]["ingredients"]["milk"]


    def price(self, drink):
        self.brew = drink
        self.drink_price = self.Menu[drink]["cost"]
        print(f"\n{drink} costs: ${self.drink_price}\n")
        
    
    def pay(self, ten, twenty, fifty):
        total = (ten * 10) / 100 + (twenty * 20) / 100 + (fifty * 50) / 100
        change = total - self.drink_price
        if total >= self.drink_price:
            print(f"Here's your {self.brew}. Enjoy!\nHere's your change: {change}")
            self.money += self.drink_price
            self.drink_price = 0.00
            total = 0
            self.reduce()
            
        else:
            print(f"Insufficient funds! You entered: ${total}. Here's your change.")
    
    
    def check_res(self):
        if self.water >= self.Menu[self.brew]["ingredients"]["water"]:
            if self.coffee >= self.Menu[self.brew]["ingredients"]["coffee"]:
                if self.milk >= self.Menu[self.brew]["ingredients"]["milk"]:
                    return True
        
