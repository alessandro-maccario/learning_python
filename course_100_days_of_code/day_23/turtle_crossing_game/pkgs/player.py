"""Class to create the player turtle and its movements"""

# --- IMPORT PACKAGES --- #
import time
from turtle import Turtle

# --- CONSTANTS --- #
MOVE_PADDLE = 30
ALIGNMENT = "center"
FONT = "Courier New"


# --- CREATE PADDLE CLASS --- #
class Player(Turtle):
    def __init__(self, starting_position: str, shape: str = "turtle") -> None:
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
        self.color("black")
        self.fillcolor("blue")
        self.shapesize(stretch_wid=1.2, stretch_len=1.2)
        self.up()
        # setheading north because it's where the turtle will go
        self.setheading(90)
        self.goto(starting_position)

    def move_up(self):
        """Move the turtle UP using the key strokes"""
        # move the paddle
        self.goto(self.xcor(), self.ycor() + MOVE_PADDLE)

    def move_down(self):
        """Move the turtle DOWN using the key strokes"""
        # move the paddle
        self.goto(self.xcor(), self.ycor() - MOVE_PADDLE)
