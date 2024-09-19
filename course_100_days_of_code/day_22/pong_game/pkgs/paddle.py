"""Class to create the paddles and their movements"""

# --- IMPORT PACKAGES --- #
from turtle import Turtle

# --- CONSTANTS --- #
MOVE_PADDLE = 30
UP = 90
DOWN = 270
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# --- CREATE PADDLE CLASS --- #
class Paddle:
    def __init__(self, starting_position: str) -> None:
        """Initialization method for the Paddle class.

        Parameters
        ----------
        starting_position : str
            Define where the puddle should be placed, either left or right on the screen.
        """
        # instantiate the turtle object by creating the starting body of the paddle with 3 squares
        self.paddle_pieces = []
        self.starting_position = starting_position
        self.create_paddle()  # initialize the create_paddle method
        self.head = self.paddle_pieces[0]  # grab just the head of the paddle

        print(self.head.heading())

    def create_paddle(self):
        """Create the turtle and position it"""
        turtle = Turtle(shape="square")
        turtle.color("White")
        turtle.fillcolor("white")
        turtle.up()
        turtle.goto(self.starting_position)
        turtle.shapesize(stretch_len=5, stretch_wid=1)
        turtle.setheading(UP)
        self.paddle_pieces.append(turtle)

    def move_up(self):
        """Move the turtle UP using the key strokes"""
        # move the paddle
        self.head.forward(MOVE_PADDLE)

    def move_down(self):
        """Move the turtle DOWN using the key strokes"""
        # move the paddle
        self.head.backward(MOVE_PADDLE)