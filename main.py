import random
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # changes color of the screen to black
screen.title("My Snake Game")
screen.tracer(0)  # tracer basically turns off the animation we see at the start of the program. can use turtle.update when this is off
# until we call turtle.update, the screen is not going to refresh
# segments = []
# x_positions = [0, -20, -40]
# for x in range(3):
#     segment = Turtle("square")
#     segment.color("white")
#     segment.penup()
#     segment.goto(x_positions[x], 0)
#     segments.append(segment)
# screen.update()  # here is where our snake body shows up in entirety.
snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.display_score()
screen.listen()
screen.onkey(fun=snake.up , key="Up")
screen.onkey(fun=snake.down , key="Down")
screen.onkey(fun=snake.left , key="Left")
screen.onkey(fun=snake.right , key="Right")
game_is_on = True
while game_is_on is True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food:
    if snake.head.distance(food) < 15:
        food.locate_food()
        snake.extend_snake()
        scoreboard.clear()
        scoreboard.increment()
        scoreboard.display_score()

    # Detect collision with wall:
    if snake.head.xcor ()> 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        print("Collided!")
        scoreboard.reset_game()
        snake.reset_snake()
    # Detect collision with itself
    for segment in snake.segments:
        x = segment.xcor()
        y = segment.ycor()
        if segment != snake.head:
            if snake.head.xcor() == x and snake.head.ycor() == y:
                scoreboard.reset_game()
                snake.reset_snake()
screen.exitonclick()
