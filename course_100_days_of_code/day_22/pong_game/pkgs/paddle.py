"""Class to create the paddles and their movements"""

# --- IMPORT PACKAGES --- #
from turtle import Turtle

# --- CONSTANTS --- #
MOVE_PADDLE = 30


# --- CREATE PADDLE CLASS --- #
class Paddle(Turtle):
    def __init__(self, starting_position: str, shape: str = "square") -> None:
        """Initialization method for the Paddle class.

        Parameters
        ----------
        starting_position : str
            Define where the puddle should be placed, either left or right on the screen.
        """
        # by using the super method, we are able to use the attributes and methods from the parent class in the child class;
        # This means that we are creating a turtle object by grabbing the attributes/methods from the parent class
        super().__init__(shape)
        # instantiate the turtle object by creating the starting body of the paddle
        self.color("White")
        self.fillcolor("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.up()
        self.goto(starting_position)

    def move_up(self):
        """Move the turtle UP using the key strokes"""
        # move the paddle
        self.goto(self.xcor(), self.ycor() + MOVE_PADDLE)

    def move_down(self):
        """Move the turtle DOWN using the key strokes"""
        # move the paddle
        self.goto(self.xcor(), self.ycor() - MOVE_PADDLE)
