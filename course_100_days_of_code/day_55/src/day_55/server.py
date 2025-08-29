"""
# Higher or Lower URLs
1. Create a new project in PyCharm called higher-lower, add a server.py file.
2. Create a new Flask application where the home route displays an <h1> that says "Guess a number between 0 and 9" and display a gif of your choice from giphy.com.
Example: https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif
3. Generate a random number between 0 and 9 or any range of numbers of your choice.
4. Create a route that can detect the number entered by the user e.g "URL/3" or "URL/9"
and checks that number against the generated random number.
- If the number is too low, tell the user it's too low,
- If the number is too high, tell the user it's too high
- If the number is the correct one, tell the user they have found the correct one.

Try to make the <h1> text a different colour for each page.
e.g. If the random number was 5 and the guess too low:
- text in red and gif about a too low number
"""

# Day 55: Advanced Decorators, Rendering HTML, Parsing URLs and Flask Debugging

from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def homepage_guess_a_number():
    return "<h1>Guess a number between 0 and 9</h1><img src='https://i.giphy.com/3o7aCSPqXE5C6T8tBC.webp'>"


# create a random number each run of the server
random_number = random.randint(0, 9)
print(random_number)


@app.route("/<guess_user_input>")
def check_number(guess_user_input: int):
    if int(guess_user_input) < random_number:
        return "<h1 style='color:DodgerBlue;'>The guessed number is too low!</h1><img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaG12dXB1NnoxbGN4dTV6b3ZwOHRrYmkzZDR3aXJhNzVsaW9qcGQ1OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TgmiJ4AZ3HSiIqpOj6/giphy.gif'>"
    elif int(guess_user_input) > random_number:
        return "<h1 style='color:Tomato;'>The guessed number is too high!</h1><img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTB4b2RrMTJtYm1vbW8zcnRnaXBodHdyZXprZTIwbTNpdW1semxwdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3og0IuWMpDm2PdTL8s/giphy.gif'>"
    else:
        return "<h1 style='color:MediumSeaGreen;'>The guessed number is too CORRECT!</h1><img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnRieTJueWJ5ZnVkYXkwcWZwZTUzdjIwaWpxaDFqeXlmNzR3aGJxMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7abKhOpu0NwenH3O/giphy.gif'>"


if __name__ == "__main__":
    # run the app in debug mode to auto-reload the server
    app.run(debug=True)
