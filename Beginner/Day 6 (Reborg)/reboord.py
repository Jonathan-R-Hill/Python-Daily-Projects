# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# Hurdle 1 / 2

def turnright():
    turn_left()
    turn_left()
    turn_left()
    
def hurdle1():
    move()
    turn_left()
    move()
    turnright()
    move()
    turnright()
    move()
    turn_left()
    
while not at_goal():
    hurdle1()


#######

# Hurdle 3 / 4 /   maze

def turnright():
    turn_left()
    turn_left()
    turn_left()
    
def hurdle3():
    if front_is_clear() and wall_on_right():
        move()
    elif right_is_clear():
        turnright()
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
     
    
while not at_goal():
    hurdle3()


