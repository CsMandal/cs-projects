from turtle import Turtle

FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 1
        self.color('black')
        self.penup()
        self.goto(-280, 240)
        self.score_details()

    def update(self):
        self.clear()
        self.score += 1
        self.score_details()

    def game_over(self):
        self.goto(-150, 0)
        self.write(f"Game Over!! score-{self.score}", align='left', font=FONT)

    def score_details(self):
        self.write(f"level {self.score}", align='left', font=FONT)

