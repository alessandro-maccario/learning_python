"""Class to create the ball and its movements"""

# --- IMPORT PACKAGES --- #
from turtle import Turtle

# --- CONSTANTS --- #
BALL_WIDTH = BALL_HEIGHT = 20
x_pos = 0
y_pos = 0


class Ball(Turtle):
    def __init__(self, shape: str = "circle") -> None:
        super().__init__(shape)

        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("White")
        self.fillcolor("white")
        self.up()
        self.goto((0, 0))

    def ball_movement(self):
        self.goto(self.xcor() + 1, self.ycor() + 1)
