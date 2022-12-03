import os

play = True
entries = [
    
]

def new_entry(name, bid):

    entries.append(
        {
        "name" : name, 
        "bid" : bid
        }
    )

def winner():
  
    top_bidder = {"name" : "", "bid" : 0}
    
    for i in entries:
        value = i["bid"]

        if value > top_bidder["bid"]:
            top_bidder = i
            
    name, bid = top_bidder["name"], top_bidder["bid"]
    print(f"The winner is {name} with a bid of {bid}!")


def anymore():
    global play
    check = input("Anymore bidders? Y or N\n").capitalize()
    
    if check == "Y":
        play = True
        
    else:
        play = False


while play:
    bid_name = input("Enter your name:  ")
    bid_val = float(input("Enter your bid:  "))
    new_entry(bid_name, bid_val)
    clear = lambda: os.system('cls')
    clear()
    anymore()
    
winner()

