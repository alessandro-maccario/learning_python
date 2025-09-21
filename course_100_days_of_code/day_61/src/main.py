from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, InputRequired
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


class MyForm(FlaskForm):
    userEmail = StringField("Email")
    userPassword = StringField("Password")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
