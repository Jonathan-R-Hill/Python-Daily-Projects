import Machine

CD = Machine.Res_Data()
valid = ["espresso", "latte", "cappuccino", "report"]

while True:
    
    choice = ''
    while choice not in valid:
        choice = input("What would you like?\nlatte\nespresso\ncappuccino\nreport\n\n").lower()
        if choice not in valid:
            print("Please type carefully!\n")

    
    if choice == "report":
        CD.report()
    else:
        CD.price(drink = choice)
        
        check = CD.check_res()
        if check == True:
            payment10 = int(input("How many Tens?   "))
            payment20 = int(input("How many Twenties?   "))
            payment50 = int(input("How many Fifties?   "))
            CD.pay(payment10, payment20, payment50)
            
        else:
            print("\nSorry! we don't have the materials to make that drink please do 'Report'\n")
