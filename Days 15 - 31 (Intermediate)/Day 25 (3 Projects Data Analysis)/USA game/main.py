import turtle
import pandas
from John import John

# Storage for variables and lists
guessed = []

num_states = 50
lives = 20

john = John()


data = pandas.read_csv("50_states.csv")
states = data.state

def check_answer(answer):
    global num_states
    global lives
    
    data_list = data.state.to_list()
    
    if answer in data_list and answer not in guessed:
        add_answer(answer)
        guessed.append(answer)
        num_states -= 1
    elif answer in guessed:
        pass
    else:
        lives -= 1


def add_answer(answer):
    new_state = data[data.state == str(answer)]
    x = new_state.x.to_list()
    y = new_state.y.to_list()
    
    john.x = int(x[0])
    john.y = int(y[0])
    john.state = answer
    john.write_on_map()
    
    
# Setting up the screen
screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_us.gif"
screen.addshape(image)
turtle.shape(image)

# Screen prompt to enter a answer
while num_states > 0 and lives > 0:
    num = len(guessed)
    answer = screen.textinput(title = f"{num}/50 correct", prompt = "Name a US State").title()
    check_answer(answer)


john.game_over()

screen.exitonclick()