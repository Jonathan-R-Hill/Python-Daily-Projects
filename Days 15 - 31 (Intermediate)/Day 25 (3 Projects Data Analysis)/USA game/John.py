from turtle import Turtle

class John(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red")
        self.hideturtle()
        self.x = 0
        self.y = 0
        self.state = ""
    
    def write_on_map(self):
        self.goto(self.x, self.y)
        self.write(arg = self.state, align = "center")
    
    def game_over(self):
        self.goto(0, 300)
        self.write(arg = "Game over you ran out of lives")
        