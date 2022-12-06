from random import randint

def play():
    numbers = list(range(0, 101))
    score = 0
    game = True
    
    num1 = numbers[randint(0, 100)]
    num2 = numbers[randint(0, 100)]
    print("Welcome to higher or lower! How far can you get?")
    
    while game == True:
        print(f"Current Number:  {num1}")
        guess = input("Higher or Lower?\n").lower()
        
        if guess == "lower":
            if num1 >= num2:
                score += 1
                print(f"That is correct! Score: {score}")
            
            else:
                print(f"The number was {num2}")
                game = False
            
        elif guess == "higher":
            if num1 <= num2:
                score += 1
                print(f"That is correct! Score: {score}")
            
            else:
                print(f"The number was {num2}")
                game = False
                
        num1 = num2
        num2 = numbers[randint(0, 100)]
    
    print(f"Game over! your score was {score}")

play()