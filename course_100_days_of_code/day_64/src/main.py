from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Text, desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables

############
# Initialize the app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
Bootstrap5(app)


################
### Database ###
class Base(DeclarativeBase):
    pass


# Once you’ve defined a base class, create the db object using the SQLAlchemy constructor
db = SQLAlchemy(model_class=Base)


# Define the table schema
# Subclass db.Model to create a model class. Define the model to create the table
class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[str] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(Text, nullable=True)
    img_url: Mapped[str] = mapped_column(Text, nullable=True)


############
# CREATE DB
# get current file path for project folder and define location for saving the db
file_path = os.path.abspath(os.getcwd()) + "/day_64/src/instance/"

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{file_path}movie-list.db"
# initialize the app with the extension
db.init_app(app)

############
# CREATE TABLE
with app.app_context():
    db.create_all()


############
# CREATE CRUD OPERATIONS
class AddMovie(FlaskForm):
    """Flask WTF fields to insert a new unique movie

    Parameters
    ----------
        FlaskForm (Class): Inherit from Flask Form
    """

    title = StringField("Movie Name", validators=[DataRequired()])
    year = IntegerField("Year", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    rating = FloatField("Rating", validators=[DataRequired()])
    ranking = IntegerField("Ranking")
    review = StringField("Review")
    img_url = StringField("Image URL")
    # submit button
    submit = SubmitField("Add a New Movie")


class EditRating(FlaskForm):
    edit_rating = StringField("New Rating", validators=[DataRequired()])
    submit = SubmitField("Edit Rating")


############
# ROUTES
@app.route("/")
def home():
    # query the book table and select all the entries ordered by book title
    movies = db.session.execute(db.select(Movie).order_by(desc(Movie.rating))).scalars()
    return render_template("index.html", movie_list=list(movies))


# Endpoint for adding a record
@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        # create new book object
        movie = Movie(
            title=request.form["title"],
            year=request.form["year"],
            description=request.form["description"],
            rating=request.form["rating"],
            ranking=request.form["ranking"],
            review=request.form["review"],
            img_url=request.form["img_url"],
        )
        db.session.add(movie)
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("add.html", form=form)


# Endpoint for editing a record
@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    form = EditRating()
    if form.validate_on_submit():
        # fetch the correct book id to be edited
        movie_to_update = db.session.execute(
            db.select(Movie).where(Movie.id == movie_id)
        ).scalar_one()
        # add the new rating to the same book to update
        movie_to_update.rating = request.form["edit_rating"]
        # commit to update the previous rating
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie_id=movie_id)


# Endpoint for deleting a record
@app.route("/delete/<int:movie_id>", methods=["GET", "DELETE"])
def delete(movie_id):
    # search for the book to remove from the db
    movie_to_delete = db.session.execute(
        db.select(Movie).where(Movie.id == movie_id)
    ).scalar()
    db.session.delete(movie_to_delete)
    # commit to update the previous rating
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
