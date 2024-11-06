import os
import sys
import html
import requests

# import hupper  # for interactive update of the tkinter window after every changes to the code
import hupper  # for interactive update of the tkinter window after every changes to the code

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.UI import TriviaQuizUI
from pkgs.constants import BASE_API_URL, QUESTION_TEST

# define the parameter for the query (currently, only True/False)
params = {"amount": 10, "difficulty": "easy", "type": "boolean"}
# send a request to the Open Trivia API
otapi_request = requests.get(BASE_API_URL, params=params)
otapi_content = otapi_request.json()["results"]

# TODO:
# 1. create a dictionary where the key is the question and the value is the answer
# 2. pick one random question at a time and pass it inside the text to be shown in the canvas
# TODO: 3. need to check if the answer is correct once the buttons are pressed. If yes,
# TODO: need to update the score and show it inside the window

# 1. create a dictionary where the key is the question and the value is the answer
question_dict = {}
for each_question in otapi_content:
    question = html.unescape(each_question["question"])
    correct_answer = html.unescape(each_question["correct_answer"])

    if question not in question_dict:
        question_dict[question] = correct_answer
    question_dict.update({question: correct_answer})


def start_reloader():
    """Reload the app at every changes in the code"""
    hupper.start_reloader("app.main")


def main():
    # Instantiate the TriviaQuizUI
    trivia_quiz_ui = TriviaQuizUI(question_dict=question_dict)

    is_game_on = True
    while is_game_on:
        # stop the game when reached the end of the list of question
        is_game_on = False


if __name__ == "__main__":
    # main()
    start_reloader()
