from turtle import Turtle
from random import randint
from time import sleep

class Creation:
    def __init__(self):
        self.turtle_list = []
        self.colors = ["red", "white", "blue", "orange", "yellow"]
        self.posx = -300
        self.posy = -100
        self.color = ''
        self.name = self.color
        self.finish = 400
        self.play = True
        self.user_bet = ''
        
    
    def draw_finish(self):
        John = Turtle()
        John.color("white")
        John.hideturtle()
        John.penup()
        John.goto(self.finish, -200)
        John.left(90)
        John.pendown()
        for _ in range(25):
            John.fd(7)
            John.penup()
            John.fd(7)
            John.pendown()
            
            
    def create(self):
        self.draw_finish()
        for i in self.colors:
            self.color = i
            i = Turtle(shape = "turtle")
            i.speed(40)
            i.color(self.color)
            self.turtle_list.append(i)
            
        self.set_pos()
    
    def set_pos(self):
        for turt in self.turtle_list:
            turt.penup()
            turt.goto(self.posx, self.posy)
            self.posy += 40
    
    def move(self):
        for turt in self.turtle_list:
            turt.fd(randint(5, 40))
            sleep(0.1)
            self.winner()
            if self.play == False:
                break
            sleep(0.1)
    
    def bet(self):
        for color in self.colors:
            print(color)
        while self.user_bet not in self.colors:
            bet = input(f"\nPlace your bet!\n")
            if bet in self.colors:
                self.user_bet == bet
                break

          
    def winner(self):
        for turt in self.turtle_list:
            if turt.xcor() >= self.finish:
                print(f"{turt.color()[0]} wins!\n")
                if self.user_bet == self.winner:
                    print(F"You won!")
                else:
                    print(F"You lost!")
                self.play = False
        
    
    
            
            