from random import randint

list_words = ["dreamcatcher", "itzy", "twice", "momoland", "new jeans", "iu", "blackpink", "loona"]
word_guess = []
list_already_guessed = []

lives = 5
word = ''
mypick = ''

def get_word():
    
    global word

    word = list_words[randint(0, len(list_words) - 1)]
    for i in range(len(word)):
        if i == " ":
            word_guess.append(" ")
        
        else:
            word_guess.append("_")
    

def player_pick():
    
    pick = ''
    
    while True:
        pick = input("Pick a letter to guess!:  ")
        
        if pick in list_already_guessed:
            print(f"You have already guessed: {pick}! ")
            print(f"You have guessed the following: {list_already_guessed}")
        
        else:
            list_already_guessed.append(pick)
            global mypick
            mypick = pick
            break


def check_in_word():
    
    num = 0
    
    if mypick in word:
        for i in word:
            if i == mypick:
                word_guess[num] = mypick
                if num == len(word) - 1:
                    break
            num += 1
            
    else:
        global lives
        lives -= 1
        print(f"{mypick} is not in the word!\n")
        

def won():
    
    if word == ''.join(word_guess):
        
        print("You have won!")
        return True


play = input("Would you like to play? Y or N\n").capitalize()
if play == "Y":
    
    get_word()
    while lives > 0:
        
        print(''.join(word_guess))
        player_pick()
        check_in_word()
        
        print(f"Lives left: {lives} \n")
        
        if won():
            break


else:
    print("You chose not to play.")

