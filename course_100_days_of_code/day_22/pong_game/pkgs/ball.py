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

        # Movement step size for x and y directions
        self.x_move = 0.3  # larger values will move the ball faster and viceversa
        self.y_move = 0.3

    def ball_movement(self):
        """Keep the ball moving based on a certain amount"""
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def wall_bouncing(self):
        """If the ball hits the wall, then change the y_move direction"""
        self.y_move *= -1

    def paddle_bouncing(self):
        """Revert the x_move direction"""
        self.x_move *= -1

    def restart(self):
        # send the ball to the homebase
        self.home()
        # start again the ball movement in reverse
        self.paddle_bouncing()
