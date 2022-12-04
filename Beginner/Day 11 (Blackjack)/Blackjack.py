from random import randint

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
ai_hand = []

player_total = 0
ai_total = 0

playing = True

def play():
    check = input("Do you want to play blackjack? Y or N\n").capitalize()
    
    if check == "Y":
        playing = True
        return playing
    else:
        playing = False
        return playing
        
def deal():
    for _ in range(2):
        player_hand.append(cards[randint(0, 12)])
        ai_hand.append(cards[randint(0, 12)])
    
    print(f"Your cards are: {player_hand}")


def check_score():
    global player_total
    global ai_total
    
    total = 0
    for i in player_hand:
        total += i
    
    aitotal = 0
    for i in ai_hand:
        aitotal += i
    
    player_total = total
    ai_total = aitotal
    
    


def player_turn():
    global player_total
    
    while True:
        
        check_score()
        print(f"Player total: {player_total}")
        
        if player_total > 21:
            print("You bust! You lose.")
            player_total = 0
            
            for _ in range(len(player_hand)):
                player_hand.pop()
                
            break
        
        check = input("Do you want to hit or hold?   ").lower()
        
        if check == "hit":
            player_hand.append(cards[randint(0, 12)])
            print(f"Your cards are: {player_hand}")

        else:
            print(f"You chose to hold. your total is: {player_total}")
            break

def ai_turn():
    global ai_total
    
    while ai_total < player_total:
        check_score()
        
        if ai_total > 21:
            print("The AI bust!.")
            ai_total = 0
            
            for _ in range(len(ai_hand)):
                ai_hand.pop()
            break
        
        if ai_total > player_total:
            break
        ai_hand.append(cards[randint(0, 12)])


print(logo)
play()
deal()
player_turn()

if player_total <=21:
    ai_turn()

if player_total > ai_total:
    print(f"You won!  You scored: {player_total}!  AI Scored: {ai_total}")
    
elif player_total < ai_total:
    print(f"You lost!  You scored: {player_total}!  AI Scored: {ai_total}")

elif player_total == ai_total:
    print(f"It's a draw!  You scored: {player_total}!  AI Scored: {ai_total}")
