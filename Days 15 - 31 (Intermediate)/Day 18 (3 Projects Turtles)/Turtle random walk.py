from turtle import Turtle, Screen
from random import randint

John = Turtle()
John.color("white")
John.shape("circle")
John.speed(10)

screen = Screen()
screen.bgcolor("black")
screen.colormode(255)

class Random_Walk:
    def __init__(self):
        self.dist_move = 40
        self.angles = [0, 90, 180, -90]
        self.angle = 0
        self.color = 0
        
    def ran_color(self):
        self.color = randint(10, 255), randint(10, 255), randint(10, 255)
    
    def pick_angle(self):
        self.angle = self.angles[randint(0, (len(self.angles) - 1))]
    
    def move(self):
        self.pick_angle()
        self.ran_color()
        John.color(self.color)
        John.right(self.angle)
        John.fd(self.dist_move)


random_move = Random_Walk()

num = 0
while num < 50:
    John.pensize(5)
    random_move.move()
    num += 1

screen.exitonclick()