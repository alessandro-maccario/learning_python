from random import randint


class Shape:
    side_length = 50

    def __init__(self, turtle_color=None) -> None:
        pass

    def random_color(self) -> str:
        """Generate a random color in hex format."""
        return "#%06x" % randint(0, 0xFFFFFF)

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
        turtle_color = self.random_color()
        turtle.color(turtle_color)

        for _ in range(0, number_of_sides):
            turtle.forward(self.side_length)
            turtle.left(360 / number_of_sides)

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
