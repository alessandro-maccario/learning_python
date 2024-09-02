from random import randint


class Shape:
    side_length = 50

    def __init__(self, turtle_color=None) -> None:
        pass

    def random_color(self) -> str:
        """Generate a random color in hex format."""
        return "#%06x" % randint(0, 0xFFFFFF)

    def square(self, turtle: object, turtle_color: str = None) -> None:
        """Draw a square using a turtle object

        Parameters
        ----------
        turtle : object
            The turtle object used to draw.
        turtle_color: str
            The turtle color object used to draw.
        """
        turtle.home()  # Move turtle to the origin – coordinates (0,0)
        # define a color for the turtle
        turtle_color = self.random_color()
        turtle.color(turtle_color)
        # --- Draw a square --- #
        """
        The underscore is a convention meaning "doesn't matter what this is". 
        So the loop will iterate n times, but without making use of a classic iteration counter. 
        Technically the iteration counter does still exist, 
        but if you're going to actually USE it, you'd rename it to something else
        """
        for _ in range(0, 4):
            turtle.forward(self.side_length)
            turtle.left(90)

        return

    def triangle(self, turtle: object, turtle_color: str = None) -> None:
        """Use the turtle object to draw a triangle

        Parameters
        ----------
        turtle : object
            The turtle object used to draw.
        """
        # define a color for the turtle
        turtle_color = self.random_color()
        turtle.color(turtle_color)

        for _ in range(0, 3):
            turtle.forward(self.side_length)
            turtle.left(120)
        return

    def pentagon(self, turtle: object, turtle_color: str = None) -> None:
        """Use the turtle object to draw a pentagon

        Parameters
        ----------
        turtle : object
            The turtle object used to draw.
        """
        # define a color for the turtle
        turtle_color = self.random_color()
        turtle.color(turtle_color)

        for _ in range(0, 5):
            turtle.forward(self.side_length)
            turtle.left(72)
        return

    def hexagon(self, turtle: object, turtle_color=None) -> None:
        """Use the turtle object to draw a pentagon

        Parameters
        ----------
        turtle : object
            The turtle object used to draw.
        """
        # define a color for the turtle
        turtle_color = self.random_color()
        turtle.color(turtle_color)

        for _ in range(0, 6):
            turtle.forward(self.side_length)
            turtle.left(60)
        return

    def heptagon(self, turtle: object, turtle_color: str = None) -> None:
        """Use the turtle object to draw a pentagon

        Parameters
        ----------
        turtle : object
            The turtle object used to draw.
        """
        # define a color for the turtle
        turtle_color = self.random_color()
        turtle.color(turtle_color)

        for _ in range(0, 7):
            turtle.forward(self.side_length)
            turtle.left(51.43)
        return

    def octagone(self, turtle: object, turtle_color: str = None) -> None:
        """Use the turtle object to draw a pentagon

        Parameters
        ----------
        turtle : object
            The turtle object used to draw.
        """
        # define a color for the turtle
        turtle_color = self.random_color()
        turtle.color(turtle_color)

        for _ in range(0, 8):
            turtle.forward(self.side_length)
            turtle.left(45)
        return

    def nonagone(self, turtle: object, turtle_color: str = None) -> None:
        """Use the turtle object to draw a pentagon

        Parameters
        ----------
        turtle : object
            The turtle object used to draw.
        """
        # define a color for the turtle
        turtle_color = self.random_color()
        turtle.color(turtle_color)

        for _ in range(0, 9):
            turtle.forward(self.side_length)
            turtle.left(40)
        return

    def decagone(self, turtle: object, turtle_color: str = None) -> None:
        """Use the turtle object to draw a pentagon

        Parameters
        ----------
        turtle : object
            The turtle object used to draw.
        """
        # define a color for the turtle
        turtle_color = self.random_color()
        turtle.color(turtle_color)

        for _ in range(0, 10):
            turtle.forward(self.side_length)
            turtle.left(36)
        return

    def dashed_line(self, turtle: object) -> None:
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
