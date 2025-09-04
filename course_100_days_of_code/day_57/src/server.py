"""
Day 57: Templating with Jinja in Flask Applications

Reference:
- https://codepen.io/candytale55/pen/EaVExNX
"""

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    current_year = datetime.now().year
    return render_template("index.html", current_year=current_year)


if __name__ == "__main__":
    # run the app in debug mode to auto-reload the server
    app.run(debug=True)
