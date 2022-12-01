print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


def game():
    section_1 = input("You are at a T junction! Which way will you go? Left OR Right?\n").capitalize()
    if section_1 == 'Left':
        
        print("Wow! you made it!")
        section_2 = input("You arrive at a river. Do you Swim OR take the boat?  Enter either: Swim OR Boat.\n").capitalize()
        
        if section_2 == "Boat":
            
            print("You made it across. And as a bonus you are nice and dry!")
            section_3 = input("There are 3 doors in front of you.. A red one, a Blue one and a Green one.\n which door do you go throug? Red, Green or Blue\n").capitalize()
            
            if section_3 == "Red":
                print("Amazing! You have found the treasure chest! The loot is yours!")
                
            elif section_3 == "Blue":
                print("You fell out of the world!  RIP")
                
            else:
                print("You end up in a room alone with no way out!  RIP")
            
        else:
            print("Oh no! you got cramp and fell to the bootom of the ocean. RIP")  
            

    else:
        print("Oh no you're lost")

game()