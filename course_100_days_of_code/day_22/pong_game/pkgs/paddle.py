"""Class to create the paddles and their movements"""

# --- IMPORT PACKAGES --- #
from turtle import Turtle

# --- CONSTANTS --- #
MOVE_SNAKE = 20
UP = 90
DOWN = 270
STARTING_POSITIONS = [(0, 0), (0, -20), (0, -40), (0, -60), (0, -80)]


# --- CREATE PADDLE CLASS --- #
class Paddle:
    def __init__(self) -> None:
        # instantiate the turtle object by creating the starting body of the turtle with 3 squares
        self.snake_bodies = []
        self.starting_position = 0
        self.create_snake()  # initialize the create_snake method
        self.head = self.snake_bodies[0]  # grab just the head of the snake

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Create the turtle and position it"""
        turtle = Turtle(shape="square")
        turtle.color("White")
        turtle.fillcolor("black")
        turtle.up()
        turtle.goto(position)
        turtle.shapesize(stretch_len=1, stretch_wid=1)
        self.snake_bodies.append(turtle)
        self.starting_position -= 20

    def move_up(self):
        """Move the turtle UP using the key strocks"""
        if (
            self.head.heading() != DOWN  # get the direction of the header of the turtle
        ):  # in the official snake game going backward was not allowed
            self.head.setheading(UP)

    def move_down(self):
        """Move the turtle DOWN using the key strocks"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
