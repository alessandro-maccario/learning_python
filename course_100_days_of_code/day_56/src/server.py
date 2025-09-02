"""
Day 56: Final Project - Name Card Website Template

Reference:
- https://codepen.io/candytale55/pen/EaVExNX
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index_2.html")


if __name__ == "__main__":
    # run the app in debug mode to auto-reload the server
    app.run(debug=True)
