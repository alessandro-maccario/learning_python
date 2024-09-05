from random import randint


class HirstPaint:
    def __init__(
        self,
        turtle: object,
        DOT_SIZE: int,
        SPACING: int,
        X_AXIS_POSITION: float,
        y_axis_position: float,
        number_of_loops: int,
    ) -> None:
        self.turtle = turtle
        self.DOT_SIZE = DOT_SIZE
        self.SPACING = SPACING
        self.X_AXIS_POSITION = X_AXIS_POSITION
        self.y_axis_position = y_axis_position
        self.number_of_loops = number_of_loops

    def hirst_paint(self) -> None:
        for _ in range(self.number_of_loops):  # loop over the number of columns
            for _ in range(self.number_of_loops):  # loop over the number of rows
                self.turtle.dot(self.DOT_SIZE, random_color())
                self.turtle.penup()
                self.turtle.forward(self.SPACING)
                self.turtle.pendown()

            self.turtle.penup()
            self.turtle.hideturtle()

            self.turtle.goto(self.X_AXIS_POSITION, self.y_axis_position + self.SPACING)
            # update y_axis_position
            self.y_axis_position += self.SPACING

            self.turtle.pendown()
            self.turtle.showturtle()

        return


def random_color() -> str:
    """Generate a random color in hex format."""
    return "#%06x" % randint(0, 0xFFFFFF)
