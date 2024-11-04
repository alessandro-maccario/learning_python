import os
import sys
import json
import base64
import html
import pandas as pd
import requests

# dynamically adjust the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pkgs.constants import BASE_API_URL


# define the parameter for the query
params = {"amount": 10, "difficulty": "easy"}
# send a request to the Open Trivia API
otapi_request = requests.get(BASE_API_URL, params=params)
otapi_content = otapi_request.json()["results"]

is_game_on = True
while is_game_on:
    for each_question in otapi_content:
        question = html.unescape(each_question["question"])
        print(question)
        user_answer = input("Insert your answer:")

# # Open the JSON file
# with open("day_34/trivia_questions_app/data/trivia_questions.json", "w") as f:
#     data = json.dump(otapi_content, f)
