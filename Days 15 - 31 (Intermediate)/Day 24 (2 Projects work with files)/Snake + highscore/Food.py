from turtle import Turtle
from random import randint

class Food:
    def __init__(self):
        
        self.food = ''
        self.food_pos = ''
        
    def create_food(self):
        self.food = Turtle(shape = "circle")
        self.food.penup()
        self.food.color("red")
        self.food_pos = (60, 60)
        self.food.goto(self.food_pos)
    
    def respawn_food(self):
        random_pos = (randint(-260, 260), (randint(-260, 260)))
        self.food_pos = random_pos
        self.food.goto(self.food_pos)