from turtle import Turtle

# --- CONSTANTS --- #
ALIGNMENT = "center"
FONT = "Courier New"


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__(visible=False)
        self.score_count = 0
        self.highest_score = self.read_highest_score()
        self.up()
        self.color("White")
        self.goto(x=0, y=280)
        self.update_score()

    def read_highest_score(self):
        with open(
            "C:/solutions/learning_python/learning_python_udemy/course_100_days_of_code/day_20/snake_game/pkgs/data.txt",
            mode="r",
        ) as f:
            return int(f.read())

    def update_score(self):
        self.clear()
        self.write(
            f"Score:  {self.score_count} | Highest Score: {self.highest_score}",
            align=ALIGNMENT,
            font=(FONT, 15),
        )

    def increase_score(self):
        self.score_count += 1
        # self.clear()
        self.update_score()

    # def game_over(self) -> bool:
    #     """Check if the turtle reached the end of the screen size"""
    #     self.home()
    #     self.write("Game Over", align=ALIGNMENT, font=(FONT, 15))
    #     return False

    def reset(self):
        if self.score_count > self.highest_score:
            self.highest_score = self.score_count
            with open(
                "C:/solutions/learning_python/learning_python_udemy/course_100_days_of_code/day_20/snake_game/pkgs/data.txt",
                mode="w",
            ) as f:
                f.write(str(self.highest_score))
        self.score_count = 0
        self.update_score()
