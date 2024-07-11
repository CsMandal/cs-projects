from turtle import Turtle,colormode,Screen
import random

t = Turtle()
t.speed('fastest')
colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    rgb = (r , g, b)
    return rgb


def soriograph(angle_width):
    for shape in range(360 // angle_width):
        t.circle(100)
        t.setheading(t.heading() + angle_width)
        t.color(random_color())
soriograph(5)
screen=Screen()
screen.exitonclick()

