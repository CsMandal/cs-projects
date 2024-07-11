from turtle import Turtle

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=5)
        self.color("black")
        self.goto(0,-220)
    def move_left(self):
        self.backward(30)
    def move_right(self):
        self.forward(30)

        
    