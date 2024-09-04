from random import choice, randint


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

    def spirograph(
        self, turtle: object, radius: int, angle_head: int, turtle_color: str = None
    ) -> None:
        turtle.speed(9)
        for _ in range(
            50
        ):  # need to stop the turtle when it reaches the same initial angle or setheading as when it started
            if _ == 0:
                # define a color for the turtle
                turtle_color = random_color()
                turtle.color(turtle_color)

                # Draw the circle
                turtle.circle(radius)
                turtle.setheading(angle_head)
            else:
                angle_head += 10
                # define a color for the turtle
                turtle_color = random_color()
                turtle.color(turtle_color)

                # Draw the circle
                turtle.circle(radius)
                turtle.setheading(angle_head)

        return


def random_color() -> str:
    """Generate a random color in hex format."""
    return "#%06x" % randint(0, 0xFFFFFF)


def random_walk(turtle: object, number_of_steps: int) -> None:
    """Let the turtle walk randomly on the screen.

    Requisites:
        - the turtle must have a bigger thickness than the normal line
        - each line must be of a random color

    Reference:
        Simple random walk on Z:
        - https://en.wikipedia.org/wiki/Random_walk

    Parameters
        ----------
        turtle : object
            The turtle object used to draw.
        number_of_steps : int
            Number of steps that the turtle will perform.
    """
    turtle.speed(9)
    for i in range(number_of_steps):
        # choose a random color for the turtle
        turtle_color = random_color()
        turtle.color(turtle_color)

        # where the head of the turtle will be
        direction = choice([0, 90, 180, 270])
        turtle.pensize(10)  # set the turtle thickness
        turtle.hideturtle()  # hide the turtle icon

        turtle.forward(30)
        # turtle.right(angle)
        turtle.setheading(direction)

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
