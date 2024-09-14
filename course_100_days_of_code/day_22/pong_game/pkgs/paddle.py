"""Class to create the paddles and their movements"""

# --- IMPORT PACKAGES --- #
from turtle import Turtle

# --- CONSTANTS --- #
MOVE_PADDLE = 30
UP = 90
DOWN = 270
# STARTING_POSITIONS = [(0, 0), (0, -20), (0, -40), (0, -60), (0, -80)]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
STARTING_POSITIONS = ((SCREEN_WIDTH / 2) - 30, 0)


# --- CREATE PADDLE CLASS --- #
class Paddle:
    def __init__(self) -> None:
        # instantiate the turtle object by creating the starting body of the paddle with 3 squares
        self.paddle_pieces = []
        self.starting_position = 0
        self.create_paddle()  # initialize the create_paddle method
        self.head = self.paddle_pieces[0]  # grab just the head of the paddle
        print(self.head.heading())

    def create_paddle(self):
        # for position in STARTING_POSITIONS:
        self.add_segment(STARTING_POSITIONS)

    def add_segment(self, position):
        """Create the turtle and position it"""
        turtle = Turtle(shape="square")
        turtle.color("White")
        turtle.fillcolor("white")
        turtle.up()
        turtle.goto(STARTING_POSITIONS)
        turtle.shapesize(stretch_len=5, stretch_wid=1)
        turtle.setheading(90)
        self.paddle_pieces.append(turtle)
        self.starting_position -= 20

    def move_up(self):
        """Move the turtle UP using the key strokes"""
        # move the paddle
        self.head.forward(MOVE_PADDLE)

    def move_down(self):
        """Move the turtle DOWN using the key strokes"""
        # move the paddle
        self.head.backward(MOVE_PADDLE)
