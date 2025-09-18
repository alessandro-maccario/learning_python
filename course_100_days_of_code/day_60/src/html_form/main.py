"""
CHALLENGE: Create a HTML Form in index.html so that when rendered as a webpage, this is what you see:
"""

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form["inputName"]
        password = request.form["inputPassword"]
        return f"<h1>Name: {username} | Password: {password}</h1>"
    else:
        return render_template("{{ url_for('login') }}")


if __name__ == "__main__":
    # run the app in debug mode to auto-reload the server
    app.run(debug=True)
