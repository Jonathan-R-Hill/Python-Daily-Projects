from turtle import Screen
from Turtle import Creation

screen = Screen()
screen.bgcolor("black")
screen.screensize(200, 200)

CR = Creation()


CR.create()
CR.bet()
while CR.play == True:
    CR.move()


screen.exitonclick()