from turtle import Turtle, Screen
from random import randint
colors = ["red", "blue", "white", "pink", "orange", "yellow"]

John = Turtle()
John.color("white")
John.shape("turtle")
screen = Screen()
screen.bgcolor("black")

def square():
    for _ in range(4):
        for _ in range(10):
            John.forward(10)
        John.right(90)


def circle():
    for _ in range(36):
        John.fd(10)
        John.right(10)


def dashed_square():
    for _ in range(4):
        for _ in range(5):
            John.fd(10)
            John.penup()
            John.fd(10)
            John.pendown()
        John.left(90)


def shapes(sides):
    angle = 360 / sides
    John.pencolor(colors[randint(0, (len(colors) - 1))])
    for _ in range(sides):
        John.fd(50)
        John.right(angle)

for num in range(3, 10):
    shapes(sides = num)


screen.exitonclick()