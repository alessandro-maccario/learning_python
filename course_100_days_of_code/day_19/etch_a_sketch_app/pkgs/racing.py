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
        self.turtle.forward(randint(1, 5))  # choose a random value between 1 and 2

    def wall_checker(self) -> None:
        # print(self.turtle.xcor(), self.turtle.ycor())

        if self.turtle.xcor() > 250:
            return False
