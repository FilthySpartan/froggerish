from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def move(self):
        self.forward(20)

    def reset_position(self):
        self.hideturtle()
        self.goto(0, -280)
        self.showturtle()

