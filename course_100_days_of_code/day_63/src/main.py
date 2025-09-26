from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
Bootstrap5(app)

all_books = []


class AddBook(FlaskForm):
    title = StringField("Book Name", validators=[DataRequired()])
    author = StringField("Book Author", validators=[DataRequired()])
    rating = StringField("Rating", validators=[DataRequired()])
    submit = SubmitField("Add a book")


@app.route("/")
def home():
    return render_template("index.html", book_list=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddBook()
    if form.validate_on_submit():
        new_book = {
            key: value
            for key, value in request.form.items()
            if key not in ["csrf_token", "submit"]
        }  # dict containing the content of the form entries
        all_books.append(new_book)
        return redirect(url_for("home"))
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
