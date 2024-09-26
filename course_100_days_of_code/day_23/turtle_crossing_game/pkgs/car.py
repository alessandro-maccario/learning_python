from turtle import Turtle
from random import uniform, randint


class Car(Turtle):
    # def __init__(self, turtle: Turtle, x_position: int, y_position: int) -> None:
    def __init__(self, x_position: int, y_position: int) -> None:
        super().__init__()
        # self.turtle = turtle
        self.x_position = x_position
        self.y_position = y_position
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        # Movement step size for x and y directions
        self.x_move = (
            uniform(0.09, 0.3)  # larger values will move the ball faster and viceversa
        )

    def starting_position(self) -> None:
        """Define the starting position of the turtle"""
        self.up()
        self.goto(x=self.x_position, y=self.y_position)

    def turtle_racing(self, random_y: int = 0) -> None:
        """Move the turtle forward of an int between 1 and 5"""
        self.goto(
            self.xcor() + self.x_move,
            self.ycor() + random_y,
        )

    def wall_checker(self, screen_size: int) -> bool:
        """Check if the turtle reached the end of the screen size"""
        if self.xcor() > (screen_size / 2):
            return True

    def car_flow(self):
        """If the cars goes out of the right side of the screen, make them appear again on the left side"""
        self.starting_position()
        # add a random element whenever each turtle restarts loop, in order to have more
        # randomly positioned cars
        self.turtle_racing(random_y=randint(-100, 100))

    def car_restart(self):
        self.clear()
        self.car_flow()
