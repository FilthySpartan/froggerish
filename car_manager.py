from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.shape("square")
        self.penup()
        self.generate_car()
        self.shapesize(stretch_wid=1, stretch_len=3)

    def move_left(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x, self.ycor())

    def generate_car(self):
        x_start = random.randint(340, 400)
        y_start = random.randint(-230, 230)
        self.color(random.choice(COLORS))
        self.goto(x_start, y_start)
        self.showturtle()

    def starting_cars(self):
        self.color(random.choice(COLORS))
        self.goto(random.randint(-200, 280), random.randint(-230, 230))
        self.showturtle()

    def destroy_car(self):
        self.clear()

    def reset_position(self):
        self.hideturtle()
        self.generate_car()
