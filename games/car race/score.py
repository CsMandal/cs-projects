from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('arial', 18, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.color('red')
        self.hideturtle()
        self.goto(150, 240)
        self.update()

    def update(self):
        self.write(f"Score : {self.score} ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER !! Score : {self.score} ", align=ALIGNMENT, font=FONT)

   