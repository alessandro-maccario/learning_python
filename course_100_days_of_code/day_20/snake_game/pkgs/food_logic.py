from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        # by inheriting from the super class Turtle, we can directly
        # use methods already available in the Turtle class and then
        # create other methods for our own.
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("red")
        self.speed("fastest")
        # call the food method to make it appear randomly on the screen
        self.refresh()

    def refresh(self):
        """The food will go to a new random location"""
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
