from turtle import Turtle
from random import randint


class TurtleMovement:
    def __init__(self, turtle: Turtle, x_position: int, y_position: int) -> None:
        self.turtle = turtle
        self.x_position = x_position
        self.y_position = y_position

    def starting_position(self) -> None:
        """Define the starting position of the turtle"""
        self.turtle.up()
        self.turtle.goto(x=self.x_position, y=self.y_position)

    def turtle_racing(self) -> None:
        """Move the turtle forward of an int between 1 and 5"""
        self.turtle.forward(randint(1, 5))  # choose a random value between 1 and 2

    def wall_checker(self, screen_size: int) -> bool:
        """Check if the turtle reached the end of the screen size"""
        if self.turtle.xcor() > screen_size / 2:
            return False
