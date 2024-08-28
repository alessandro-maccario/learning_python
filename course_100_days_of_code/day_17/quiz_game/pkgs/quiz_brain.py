# TODO: asking the questions to the user
# TODO: checking if the answer was correct
# TODO: checking if we are at the end of the quiz

# Example of request to the user:
# "Q.1: A slug's blood is green (True/False)?:"


class QuizBrain:
    def __init__(self, question_list) -> None:
        # this will keep track of which question we are asking to the user
        self.question_number = -1  # default value, already given
        # this is an input that we get once the instance is created
        self.question_list = question_list

    def still_has_question(self):
        """If there are still questions available, keep asking them to the user"""
        # if False, stop asking questions
        return self.question_number <= len(self.question_list)

    def next_question(self):
        self.question_number += 1
        try:
            ask_question = input(
                f"Q.{self.question_number}: {self.question_list[self.question_number]} (True/False)?: "
            )
            return ask_question
        except IndexError:
            return False
