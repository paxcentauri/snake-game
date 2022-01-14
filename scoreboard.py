from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 200)
        self.display_score()
        self.color("white")

    def display_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increment(self):
        self.score += 1

    def display_game_over(self):
        self.home()
        self.write("Game over!", align="center", font=("Arial", 24, "normal"))
