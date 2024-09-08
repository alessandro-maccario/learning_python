from turtle import Turtle

# --- CONSTANTS --- #
MOVE_SNAKE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
ALIGNMENT = "center"
FONT = "Courier New"
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self) -> None:
        # instantiate the turtle object by creating the starting body of the turtle with 3 squares
        self.snake_bodies = []
        self.starting_position = 0
        self.create_snake()  # initialize the create_snake method
        self.head = self.snake_bodies[0]  # grab just the head of the snake

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def snake_move(self):
        """
        Make the snake move. Grab the coordinates of each next segments where to send the last segment to.
        The idea here is to move the last segment to the same position of the second to last, then the
        second to last segment in the first position and finally, out of the loop, move the first segment forward by 20. And so on.
        """
        for _ in self.snake_bodies:
            for id_body_segment in range(len(self.snake_bodies) - 1, 0, -1):
                new_x = self.snake_bodies[id_body_segment - 1].xcor()
                new_y = self.snake_bodies[id_body_segment - 1].ycor()
                self.snake_bodies[id_body_segment].goto(new_x, new_y)
            self.head.forward(
                MOVE_SNAKE
            )  # move the first piece forward while the other pieces will be set to new coordinates

    def move_up(self):
        if (
            self.head.heading() != DOWN  # get the direction of the header of the turtle
        ):  # in the official snake game going backward was not allowed
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        # add a segment to the snake after the last position
        self.add_segment(
            self.snake_bodies[-1].position()
        )  # get hold of the position of the last element in the array

    def add_segment(self, position):
        turtle_body = Turtle(shape="square")
        turtle_body.color("White")
        turtle_body.fillcolor("black")
        turtle_body.up()
        turtle_body.goto(position)
        turtle_body.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.snake_bodies.append(turtle_body)
        self.starting_position -= 20
