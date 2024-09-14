"""Class to create the paddles and their movements"""

# --- IMPORT PACKAGES --- #
from turtle import Turtle

# --- CONSTANTS --- #
MOVE_PADDLE = 20
UP = 90
DOWN = 270
# STARTING_POSITIONS = [(0, 0), (0, -20), (0, -40), (0, -60), (0, -80)]
STARTING_POSITIONS = (0, 0)


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

    def move(self, direction: str) -> None:
        """
        Make the snake move. Grab the coordinates of each next segments where to send the last segment to.
        The idea here is to move the last segment to the same position of the second to last, then the
        second to last segment in the first position and finally, out of the loop, move the first segment forward by 20. And so on.
        """

        if direction == "forward":
            for _ in self.paddle_pieces:
                for id_body_segment in range(len(self.paddle_pieces) - 1, 0, -1):
                    new_x = self.paddle_pieces[id_body_segment - 1].xcor()
                    new_y = self.paddle_pieces[id_body_segment - 1].ycor()
                    self.paddle_pieces[id_body_segment].goto(new_x, new_y)
                    self.head.forward(
                        MOVE_PADDLE
                    )  # move the first piece forward while the other pieces will be set to new coordinates
        elif direction == "backward":
            for _ in self.paddle_pieces:
                for id_body_segment in range(len(self.paddle_pieces) - 1, 0, -1):
                    new_x = self.paddle_pieces[id_body_segment - 1].xcor()
                    new_y = self.paddle_pieces[id_body_segment - 1].ycor()
                    self.paddle_pieces[id_body_segment].goto(new_x, new_y)
                    self.head.backward(
                        MOVE_PADDLE
                    )  # move the first piece backward while the other pieces will be set to new coordinates

    def move_up(self):
        """Move the turtle UP using the key strocks"""
        print(self.head.heading())
        # move the paddle
        self.head.forward(MOVE_PADDLE)

    def move_down(self):
        """Move the turtle DOWN using the key strocks"""
        print(self.head.heading())
        # move the paddle
        self.head.backward(MOVE_PADDLE)
