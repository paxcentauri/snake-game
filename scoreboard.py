from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        file = open("highscore.txt", mode="r")
        hs = file.read()
        self.high_score = int(hs)
        file.close()
        self.hideturtle()
        self.penup()
        self.goto(0, 200)
        self.display_score()
        self.color("white")

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increment(self):
        self.score += 1

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        file = open("highscore.txt", mode="w")
        file.write(str(self.high_score))
        file.close()
        self.score = 0
        self.display_score()
