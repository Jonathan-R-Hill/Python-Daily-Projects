from turtle import Turtle, Screen
from Snake import Snake
from time import sleep
from Food import Food

game = Snake()
snake_food = Food()

# Game Screen
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

def movement():
        screen.onkey(game.up, "w")
        screen.onkey(game.left, "a")
        screen.onkey(game.down, "s")
        screen.onkey(game.right, "d")
        game.move()


game.create_snake()
snake_food.create_food()
game.create_scoreboard()

while game.alive == True:
    sleep(0.1)
    movement()
    if game.snakehead.distance(snake_food.food) < 15:
        snake_food.respawn_food()
        game.add_snakepart()
        game.score += 1
        game.update_score()

        
    screen.update()
    
    # Collision with wall
    if game.snakehead.xcor() > 280 or game.snakehead.xcor() < -280 or game.snakehead.ycor() > 280 or game.snakehead.ycor() < -280:
        game.alive = False
        print(f"Game Over. \nYour score was: {game.score}\n")
        
    # collision with self
    for segment in game.snakeparts[1:]:
        if game.snakehead.distance(segment) < 15:
            game.alive = False
            print(f"Game Over. \nYour score was: {game.score}\n")
    

screen.exitonclick()