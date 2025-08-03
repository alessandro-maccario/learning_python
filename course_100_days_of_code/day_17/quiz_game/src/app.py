"""
This script will create a simple Quiz Game in Python for the 100 Days of Code challenge from the Udemy course.

"""

import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.question_model import Question

# from data.data import question_data # old data
from data.data_triviadb import question_data  # data from TriviaDB
from pkgs.quiz_brain import QuizBrain

# create a list to hold all the questions
question_bank = []

# Append each question to the question_bank list as a Question() object
for idx, question_and_answer in enumerate(question_data):
    question_bank.append(
        Question(question_data[idx]["question"], question_data[idx]["correct_answer"])
    )

# instiate the QuizBrain class with the question_bank
quiz = QuizBrain(question_bank)


def main():
    global question  # make the question variable available globally
    while quiz.still_has_question():
        question = quiz.next_question()

    # End of the game
    print("You have completed this challenge!")
    print(
        f"Your final score is: {quiz.score}/ {len(quiz.question_list)} = {round(quiz.score/len(quiz.question_list), 2)*100}"
    )


# --- MAIN --- #
if __name__ == "__main__":
    main()
