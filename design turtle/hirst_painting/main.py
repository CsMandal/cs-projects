import random
from turtle import Turtle,colormode,Screen
colormode(255)
t = Turtle()
screen = Screen()


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb=(r,g,b)
    return rgb

def dot_print():
    for i in range(16):
        t.dot(20, random_color())
        t.penup()
        t.forward(40)
        t.pendown()


t.hideturtle()
t.penup()
t.setheading(212)
t.forward(350)
t.setheading(0)
t.pendown()
x, y = t.position()

for i in range(16):
    dot_print()
    t.penup()
    y += 40
    t.setposition(x,y)
    t.pendown()




screen.exitonclick()




