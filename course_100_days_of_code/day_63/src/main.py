from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables


################
### Database ###
class Base(DeclarativeBase):
    pass


# Once you’ve defined a base class, create the db object using the SQLAlchemy constructor
db = SQLAlchemy(model_class=Base)


# Subclass db.Model to create a model class. Define the model to create the table
class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)
    author: Mapped[str] = mapped_column(String)
    rating: Mapped[str] = mapped_column(String)


#################

# create the app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
Bootstrap5(app)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)

# create the tables
with app.app_context():
    db.create_all()

all_books = []


class AddBook(FlaskForm):
    title = StringField("Book Name", validators=[DataRequired()])
    author = StringField("Book Author", validators=[DataRequired()])
    rating = StringField("Rating", validators=[DataRequired()])
    submit = SubmitField("Add a book")


@app.route("/")
def home():
    books = Book.query.all()
    print(books)
    return render_template("index.html", book_list=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddBook()
    if form.validate_on_submit():
        # create new book object
        book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"],
        )
        db.session.add(book)
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
