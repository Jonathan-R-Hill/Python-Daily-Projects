from turtle import Turtle, Screen, bgcolor
import prettytable

John = Turtle()
John.color("blue")
John.shape("turtle")

# Creating the window
screen = Screen()
screen.bgcolor("black")


def move():
    
    i = 0
    while i < 4:
        for _ in range(10):
            John.forward(10)
            John.pendown()
            John.forward(10)
            John.penup()
                
        John.right(90)
        i += 1

move()

#############################################

screen.exitonclick()

table = prettytable.PrettyTable()

table.field_names = ["Pokemon Number", "Pokemon Name", "Type"]

def add(number, name, ptype):

    table.add_row([number, name, ptype])

table.align["Pokemon Number"] = "l"
table.align["Pokemon Name"] = "c"
table.align["Type"] = "r"

add(1, "bulbasaur", "grass/poison")

print(table)