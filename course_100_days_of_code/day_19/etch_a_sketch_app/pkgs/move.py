from turtle import Turtle


class TurtleMovement:
    def __init__(self, turtle: Turtle) -> None:
        self.turtle = turtle

    def going_forwards(self) -> None:
        self.turtle.forward(10)

    def going_backwards(self) -> None:
        self.turtle.backward(10)

    def going_up(self) -> None:
        self.turtle.up()

    def going_down(self) -> None:
        self.turtle.down()

    def turn_left(self) -> None:
        self.turtle.left(5)

    def turn_right(self) -> None:
        self.turtle.right(5)

    def turtle_clean(self) -> None:
        self.turtle.clear()
        self.turtle.up()
        self.turtle.home()
        self.turtle.down()
