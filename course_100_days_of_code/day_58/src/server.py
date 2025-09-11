"""
Day 58: Bootstrap

Reference:
- https://getbootstrap.com/docs/5.3/components/card/
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    # run the app in debug mode to auto-reload the server
    app.run(debug=True)
