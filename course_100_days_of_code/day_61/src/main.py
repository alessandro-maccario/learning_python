from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms import PasswordField, EmailField, SubmitField
from wtforms.validators import (
    DataRequired,
    Email,
    Length,
)
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
bootstrap = Bootstrap5(
    app
)  # using flask_bootstrap to improve webpage appearance with Flask-Bootstrap


class LoginForm(FlaskForm):
    userEmail = EmailField(
        label="Email",
        validators=[
            DataRequired(),
            Email(message="The email must contain a @ and a '.'"),
        ],
    )  # The validators parameter accepts a List of validator Objects
    userPassword = PasswordField(
        label="Password",
        validators=[DataRequired(), Length(min=8)],
    )
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if (
            form.userEmail.data == "admin@email.com"
            and form.userPassword.data == "12345678"
        ):
            return render_template("success.html", form=form)
        else:
            return render_template("denied.html", form=form)

    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
