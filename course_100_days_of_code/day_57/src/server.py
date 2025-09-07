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
    # return the name to be displayed and to be used to guess the gender
    gender_name = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    # send the variable to jinja in the html page
    return render_template(
        "guess_name.html",
        name=name,
        gender_name=gender_name,
        current_year=current_year,
    )


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    # run the app in debug mode to auto-reload the server
    app.run(debug=True)
