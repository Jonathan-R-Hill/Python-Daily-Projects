from random import randint
from turtle import Turtle


class Snake:
    def __init__(self):
        # Snake
        self.snakeparts = []
        self.snakehead = ''
        
        # Score Stuff
        self.score = 0
        self.scoreboard = ''

        # start co-ords
        self.posx = 0
        self.posy = 0
        
        # Movement
        self.alive = True
        self.direction = 'd'
        self.speed = 10
        
    def create_snake(self):
        for snake in range(0, 4):
            snake = Turtle(shape = "square")
            snake.color('white')
            snake.penup()
            snake.speed(self.speed)
            snake.goto(self.posx, self.posy)
            
            self.posx -= 20
            self.snakeparts.append(snake)
            
        self.snakehead = self.snakeparts[0]

    def up(self):
        if self.direction != 's' and self.direction != "w":
            if self.direction == 'd':
                self.snakehead.left(90)
            elif self.direction == "a":
                self.snakehead.right(90)
            self.direction = "w"
    
    def down(self):
        if self.direction != 'w' and self.direction != "s":
            if self.direction == 'd':
                self.snakehead.right(90)
            elif self.direction == "a":
                self.snakehead.left(90)
            self.direction = "s"

    def right(self):
        if self.direction != 'a' and self.direction != "d":
            if self.direction == "w":
                self.snakehead.right(90)
            elif self.direction == "s":
                self.snakehead.left(90)
            self.direction = "d"
                
    def left(self):
        if self.direction != 'd' and self.direction != "a":
            if self.direction == "w":
                self.snakehead.left(90)
            elif self.direction == "s":
                self.snakehead.right(90)
            self.direction = "a"
            
    def move(self):
        for seg in range(len(self.snakeparts)- 1, 0, -1):
            pos_x = self.snakeparts[seg - 1].xcor()
            pos_y = self.snakeparts[seg - 1].ycor()
            self.snakeparts[seg].goto(pos_x, pos_y)
        self.snakehead.forward(20)
    
    def add_snakepart(self):
        snake = Turtle(shape = "square")
        snake.color('white')
        snake.penup()
        snake.speed(self.speed)
        snake.goto(self.snakeparts[len(self.snakeparts) - 1].pos())
        self.snakeparts.append(snake)
    
    def create_scoreboard(self):
        self.scoreboard = Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.color('orange')
        self.scoreboard.penup()
        self.scoreboard.goto(0, 280)
        self.scoreboard.write(f"Score: {self.score}", align = "center")
    
    def update_score(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score}", align = "center")
    

    