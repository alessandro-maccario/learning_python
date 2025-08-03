# TODO: asking the questions to the user
# TODO: checking if the answer was correct
# TODO: checking if we are at the end of the quiz

# Example of request to the user:
# "Q.1: A slug's blood is green (True/False)?:"


class QuizBrain:
    def __init__(self, question_list) -> None:
        # this will keep track of which question we are asking to the user
        self.question_number = 0  # default value, already given
        # this is an input that we get once the instance is created
        self.question_list = question_list
        self.score = 0  # increase every time the user get the answer right

    def still_has_question(self):
        """If there are still questions available, keep asking them to the user"""
        # if False, stop asking questions
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Wrong answer.")

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number+1}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def next_question(self):
        try:
            ask_question = input(
                f"Q.{self.question_number}: {self.question_list[self.question_number].text} (True/False)?: "
            )

            self.check_answer(
                ask_question, self.question_list[self.question_number].answer
            )
            self.question_number += 1  # go to the next question
            return ask_question
        except IndexError:
            return False
