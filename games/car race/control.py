from turtle import Turtle,colormode
import random

POSITIONS = [(0,240), (150,240), (-150,240)]

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    rgb = (r , g, b)
    return rgb


class Control(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=4, stretch_wid=3)
        self.color(random_color())
        self.goto(random.choice(POSITIONS))
        self.setheading(-270)
    
    def move(self):
        self.backward(50)
    
    
        
        
    