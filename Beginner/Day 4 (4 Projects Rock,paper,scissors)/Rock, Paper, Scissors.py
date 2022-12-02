from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = ["rock", "paper", "scissors"]
win_con = [[0, -1, 1],[1, 0, -1],[-1, 1, 0]]   # 1 = win   0 = draw  -1 = loss
num = randint(0, 2)

aipick = choice[num]
player = input("Pick Rock, Paper or scissors:  ").lower()


def game(player, aipick):

    # Player display pic   
    if player in choice:
        print(f"You chose: {player}!")
        
        if player == "paper":
            print(paper)
            pos = 1
            
        elif player == "rock":
            print(rock)
            pos = 0
            
        else:
            print(scissors)
            pos = 2
    else:
        print("Invalid Choice!")
        return
        
    # AI display pic
    if aipick in choice:
        print(f"The AI chose: {aipick}!")
        if aipick == "paper":
            print(paper)
            
        elif aipick == "rock":
            print(rock)
            
        else:
            print(scissors)    

    if win_con[pos][num] == 0:
        print("It's a Draw!")
    
    elif win_con[pos][num] == -1:
        print("You Lost!")
    
    else:
        print("You Won!")

game(player, aipick)

