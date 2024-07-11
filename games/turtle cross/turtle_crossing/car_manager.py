from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()

    def create_car(self):
        random_num = random.randint(1,6)
        if random_num == 5:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = random.randint(-280, 280)
            new_car.color(random.choice(COLORS))
            new_car.goto(280, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for cars in self.all_cars:
            cars.backward(STARTING_MOVE_DISTANCE)

    def collision(self, position):
        for cars in self.all_cars:
            if cars.distance(position) < 20:
                return True




