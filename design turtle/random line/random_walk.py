from turtle import Turtle,colormode
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def color_choice():
    r=random.randint(0,255)
t = Turtle()
directions = [0, 90, 180, 270]
t.speed('fast')
t.pensize(10)
colormode(255)

for _ in range(200):
    t.color(random.choice(colours))
    t.forward(50)
    t.setheading(random.choice(directions))