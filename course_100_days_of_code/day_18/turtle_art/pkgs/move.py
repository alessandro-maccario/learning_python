from random import choice, randint, randrange


class Shape:
    side_length = 50

    def __init__(self, turtle_color=None) -> None:
        pass

    def geometric_shape(
        self, turtle: object, number_of_sides: int, turtle_color: str = None
    ) -> None:
        """Draw a geometric shape (triangle, square, ...) using a turtle object and
        by defining the number of sides that the shape must have.

        Possible shapes:
        - triangle (number of sides: 3)
        - square (number of sides: 4)
        - pentagone (number of sides: 5)
        - hexagone (number of sides: 6)
        - eptagone (number of sides: 7)
        - octagon (number of sides: 8)
        - nonagon (number of sides: 9)
        - decagon (number of sides: 10)

        Parameters
        ----------
        turtle : object
            The turtle object used to draw.
        number_of_sides : int
            Number of sides of the shape
        turtle_color: str
            The turtle color object used to draw.
        """
        turtle.setheading(0)  # Move turtle to the origin – coordinates (0,0)
        # define a color for the turtle
        turtle_color = random_color()
        turtle.color(turtle_color)

        for _ in range(0, number_of_sides):
            turtle.forward(self.side_length)
            turtle.left(360 / number_of_sides)

        return


def random_color() -> str:
    """Generate a random color in hex format."""
    return "#%06x" % randint(0, 0xFFFFFF)


def random_walk(turtle: object, number_of_steps: int) -> None:
    """Let the turtle walk randomly on the screen.

    Requisites:
        - the turtle must have a bigger thickness than the normal line
        - each line must be of a random color
    """
    for i in range(number_of_steps):
        # choose a random color for the turtle
        turtle_color = random_color()
        turtle.color(turtle_color)

        # randomly choose the movement value.
        # This can be anything, just the logic to decide right or left
        movement = choice([-1, 1])
        # define a random angle to turn the turtle head
        angle = choice([randrange(-360, 360)])
        turtle.pensize(10)  # set the turtle thickness
        turtle.hideturtle()  # hide the turtle icon

        if movement == 1:
            turtle.forward(50)
            turtle.right(angle)
        else:
            turtle.backward(50)
            turtle.left(angle)

    return


def dashed_line(turtle: object) -> None:
    """Use the turtle to draw a dashed line.

    Parameters
    ----------
    turtle : object
        The turtle object used to draw.
    """

    for _ in range(0, 10):
        turtle.forward(10)
        turtle.up()
        turtle.forward(5)
        turtle.down()
    return
