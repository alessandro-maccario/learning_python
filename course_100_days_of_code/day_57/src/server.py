"""
Day 57: Templating with Jinja in Flask Applications

Reference:
- https://codepen.io/candytale55/pen/EaVExNX
- https://genderize.io/documentation
"""

from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

# define the current year to be used in the Copyright section
current_year = datetime.now().year


@app.route("/")
def home():
    return render_template("index.html", current_year=current_year)


@app.route("/guess/<name>")
def guess_name(name: str):
    # first letter of the name must be capitalized
    capitalized_name = name.capitalize()
    # return the name to be displayed and to be used to guess the gender
    gender_name = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    # send the variable to jinja in the html page
    return render_template(
        "guess_name.html",
        name=capitalized_name,
        gender_name=gender_name,
        current_year=current_year,
    )


if __name__ == "__main__":
    # run the app in debug mode to auto-reload the server
    app.run(debug=True)
