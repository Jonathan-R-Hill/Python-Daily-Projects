from turtle import Turtle, Screen
from random import randint

John = Turtle()
John.color("white")
John.shape("circle")
John.pensize(10)
John.speed(250)
John.hideturtle()


screen = Screen()
screen.bgcolor("black")
screen.colormode(255)
screen.screensize(500, 500)

class Spots:
    def __init__(self):
        self.dist_move = 25
        self.posx = -490.00
        self.posy = -375.00
        self.totalspots = 0
        self.color = 0
        
    def ran_color(self):
        self.color = randint(10, 255), randint(10, 255), randint(10, 255)
    
    def set_pos(self):
        John.penup()
        John.setposition(self.posx, self.posy)
        John.pendown()
        
        self.posy += 30
    
    def move(self):
        self.ran_color()
        
        John.color(self.color)
        John.penup()
        John.fd(self.dist_move)
        John.pendown()
        John.fd(1)
        John.pendown()


move = Spots()
check = 0
num = 0

while move.posy < 500:
    move.set_pos()
    check += 1
    
    while John.xcor() < 425:
        move.move()
        num += 1

    num = 0


screen.exitonclick()