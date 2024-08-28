"""
This script will create a simple Quiz Game in Python for the 100 Days of Code challenge from the Udemy course.

"""

import os
import sys

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pkgs.question_model import Question
from data.data import question_data
from pkgs.quiz_brain import QuizBrain


question_bank = []

for idx, question_and_answer in enumerate(question_data):
    question_bank.append(
        Question(question_data[idx]["text"], question_data[idx]["answer"])
    )

# print(question_bank)

quiz = QuizBrain(question_bank)

#
while quiz.still_has_question():
    question = quiz.next_question()

# End of the game
print("You have completed this challenge!")
print(
    f"Your final score is: {quiz.score}/ {len(quiz.question_list)} = {round(quiz.score/len(quiz.question_list), 2)*100}"
)
