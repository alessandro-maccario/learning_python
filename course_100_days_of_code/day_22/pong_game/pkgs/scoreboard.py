from turtle import Turtle

# --- CONSTANTS --- #
ALIGNMENT = "center"
FONT = "Courier New"


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.right_score_count = 0
        self.left_score_count = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Creating the two turtles to write the score on the screen for the left and right paddle"""
        self.clear()
        # draw the left score
        self.goto(-100, 200)
        self.write(
            f"{self.left_score_count}",
            align="center",
            font=(FONT, 50),
        )
        # draw the right score
        self.goto(100, 200)
        self.write(
            f"{self.right_score_count}",
            align="center",
            font=(FONT, 50),
        )

    def right_increase_score(self):
        """Increase the score for the right paddle"""
        self.right_score_count += 1
        self.update_scoreboard()

    def left_increase_score(self):
        """Increase the score for the left paddle"""
        self.left_score_count += 1
        self.update_scoreboard()

    def game_over(self) -> bool:
        """Check if the turtle reached the end of the screen size"""
        self.home()
        self.write("Game Over", align=ALIGNMENT, font=(FONT, 15))
        return
