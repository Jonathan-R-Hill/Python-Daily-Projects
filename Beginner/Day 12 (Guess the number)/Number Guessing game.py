from random import randint
logo = """
 
 ________  ________  ________            ___    ___ ________  ___  ___                         
|\   ____\|\   __  \|\   ___  \         |\  \  /  /|\   __  \|\  \|\  \                        
\ \  \___|\ \  \|\  \ \  \\ \  \        \ \  \/  / | \  \|\  \ \  \\\  \                       
 \ \  \    \ \   __  \ \  \\ \  \        \ \    / / \ \  \\\  \ \  \\\  \                      
  \ \  \____\ \  \ \  \ \  \\ \  \        \/  /  /   \ \  \\\  \ \  \\\  \                     
   \ \_______\ \__\ \__\ \__\\ \__\     __/  / /      \ \_______\ \_______\                    
    \|_______|\|__|\|__|\|__| \|__|    |\___/ /        \|_______|\|_______|                    
                                       \|___|/                                                 
                                                                                               
                                                                                               
 ________  ___  ___  _______   ________   ________           _________  ___  ___  _______      
|\   ____\|\  \|\  \|\  ___ \ |\   ____\ |\   ____\         |\___   ___\\  \|\  \|\  ___ \     
\ \  \___|\ \  \\\  \ \   __/|\ \  \___|_\ \  \___|_        \|___ \  \_\ \  \\\  \ \   __/|    
 \ \  \  __\ \  \\\  \ \  \_|/_\ \_____  \\ \_____  \            \ \  \ \ \   __  \ \  \_|/__  
  \ \  \|\  \ \  \\\  \ \  \_|\ \|____|\  \\|____|\  \            \ \  \ \ \  \ \  \ \  \_|\ \ 
   \ \_______\ \_______\ \_______\____\_\  \ ____\_\  \            \ \__\ \ \__\ \__\ \_______\
    \|_______|\|_______|\|_______|\_________\\_________\            \|__|  \|__|\|__|\|_______|
                                 \|_________\|_________|                                       
                                                                                               
                                                                                               
 ________   ___  ___  _____ ______   ________  _______   ________  ________                    
|\   ___  \|\  \|\  \|\   _ \  _   \|\   __  \|\  ___ \ |\   __  \|\_____  \                   
\ \  \\ \  \ \  \\\  \ \  \\\__\ \  \ \  \|\ /\ \   __/|\ \  \|\  \|____|\  \                  
 \ \  \\ \  \ \  \\\  \ \  \\|__| \  \ \   __  \ \  \_|/_\ \   _  _\    \ \__\                 
  \ \  \\ \  \ \  \\\  \ \  \    \ \  \ \  \|\  \ \  \_|\ \ \  \\  \|    \|__|                 
   \ \__\\ \__\ \_______\ \__\    \ \__\ \_______\ \_______\ \__\\ _\        ___               
    \|__| \|__|\|_______|\|__|     \|__|\|_______|\|_______|\|__|\|__|      |\__\              
                                                                            \|__|              
                                                                                               
                                                           
"""
nums = list(range(0,100))


def game():
    global lives
    number_to_guess = nums[randint(0, 99)]
    
    while lives > 0:
        guess = int(input("Guess a number!\n"))
        
        if guess == number_to_guess:
            print(f"You won! the number was {number_to_guess}")
            break
        elif guess < number_to_guess:
            lives -= 1
            print(f"That was incorrect. You guessed: {guess}.\nThe number is BIGGER than this!")
        elif guess > number_to_guess:
            lives -=1
            print(f"That was incorrect. You guessed: {guess}.\nThe number is SMALLER than this!")
            
        print(f"Lives remaining: {lives}")
        
    if lives == 0:   
        print("You ran out of lives the number was: {number to guess}.\nBetter luck next time")

print(logo)      
print("Welcome to the guessing game!\nI'm thinking of a number between 1 and 100.")
play = input("Do you want to play? Y or N").capitalize()


if play == "Y":
    difficulty = input("Do you want to play on easy or hard?\n").lower()
    
    if difficulty == "easy":
        lives = 6
    else:
        lives = 3
    
    game()