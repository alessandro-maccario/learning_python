class Shape:
    def __init__(self) -> None:
        pass

    def square(self, turtle: object) -> None:
        """Draw a square using a turtle object

        Parameters
        ----------
        turtle : object
            The object used to draw.
        """
        turtle.home()  # Move turtle to the origin – coordinates (0,0)
        # --- Draw a square --- #
        for turn in range(0, 4):
            turtle.forward(50)
            turtle.left(90)

        return
