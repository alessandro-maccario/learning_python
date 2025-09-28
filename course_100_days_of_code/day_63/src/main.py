from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Float, delete
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
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
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


#################
# get current file path for project folder and define location for saving the db
file_path = os.path.abspath(os.getcwd()) + "/day_63/src/instance/"

# create the app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
Bootstrap5(app)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{file_path}new-books-collection.db"
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


class EditRating(FlaskForm):
    edit_rating = StringField("New Rating", validators=[DataRequired()])
    submit = SubmitField("Edit Rating")


@app.route("/")
def home():
    # query the book table and select all the entries ordered by book title
    books = db.session.execute(db.select(Book).order_by(Book.title)).scalars()
    return render_template("index.html", book_list=list(books))


# Endpoint for adding a record
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


# Endpoint for editing a record
@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    form = EditRating()
    if form.validate_on_submit():
        # fetch the correct book id to be edited
        book_to_update = db.session.execute(
            db.select(Book).where(Book.id == book_id)
        ).scalar_one()
        # add the new rating to the same book to update
        book_to_update.rating = request.form["edit_rating"]
        # commit to update the previous rating
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("edit.html", form=form, book_id=book_id)


# Endpoint for deleting a record
@app.route("/delete/<int:book_id>", methods=["GET", "DELETE"])
def delete(book_id):
    # search for the book to remove from the db
    book_to_delete = db.session.execute(
        db.select(Book).where(Book.id == book_id)
    ).scalar()
    db.session.delete(book_to_delete)
    # commit to update the previous rating
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
