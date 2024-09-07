from turtle import Turtle


class TurtleMovement:
    def __init__(self, turtle: Turtle, x_position: int, y_position: int) -> None:
        self.turtle = turtle
        self.x_position = x_position
        self.y_position = y_position

    def starting_position(self) -> None:
        # turtle
        self.turtle.up()
        self.turtle.goto(x=self.x_position, y=self.y_position)
