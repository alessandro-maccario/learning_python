class Shape:
    def __init__(self) -> None:
        pass

    def square(self, turtle: object) -> None:
        """Draw a square using a turtle object

        Parameters
        ----------
        turtle : object
            The turtle object used to draw.
        """
        turtle.home()  # Move turtle to the origin – coordinates (0,0)
        # --- Draw a square --- #
        """
        The underscore is a convention meaning "doesn't matter what this is". 
        So the loop will iterate n times, but without making use of a classic iteration counter. 
        Technically the iteration counter does still exist, 
        but if you're going to actually USE it, you'd rename it to something else
        """
        for _ in range(0, 4):
            turtle.forward(50)
            turtle.left(90)

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
