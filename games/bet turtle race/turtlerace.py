import turtle as t
import random

is_game_on = True
screen = t.Screen()
screen.setup(height=400, width=500)
user_color = screen.textinput(title='Choose color', prompt="bet which color turtle will win")
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
y_pos = [-60, -20, 20, 60, 100, 140]
turtle_list = []
for i in range(6):
    tin = t.Turtle(shape="turtle")
    tin.penup()
    tin.color(colors[i])
    tin.goto(x=-230, y=y_pos[i])
    turtle_list.append(tin)

while is_game_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_game_on = False
            win_color = turtle.pencolor()
            if win_color == user_color:
                print(f"you won !!! {win_color} win the race")
            else:
                print(f"you loose!!! {win_color} win the race")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
