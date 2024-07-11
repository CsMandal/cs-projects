from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('arial', 18, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.write(f"Score : {self.score}  high score {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.highscore :
            self.highscore = self.score
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.(f' Game Over'  , align=ALIGNMENT, font=FONT)