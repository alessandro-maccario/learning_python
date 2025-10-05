from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    PasswordField,
    EmailField,
    SubmitField,
    URLField,
)
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from flask_ckeditor.utils import cleanify
from datetime import date
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
Bootstrap5(app)
# Initializes CKEditor and binds it to your Flask app instance
ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


# get current file path for project folder and define location for saving the db
file_path = os.path.abspath(os.getcwd()) + "/day_67/src/instance/"
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{file_path}posts.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


# Define the New Post Form
class NewPost(FlaskForm):
    title = StringField(
        label="Blog Post Title",
        validators=[
            DataRequired(),
        ],
    )
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    author_name = StringField(label="Author's Name", validators=[DataRequired()])
    background_image_url = URLField(
        label="Background Image URL", validators=[DataRequired(), URL()]
    )
    body = CKEditorField(label="Body Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit Post")


@app.route("/")
def get_all_posts():
    # Query the database for all the posts. Convert the data to a python list. If you do .all() on a Result, you get a list of rows (list of tuples/dicts).
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)


# Add a route so that you can click on individual posts.
@app.route("/<post_id>")
def show_post(post_id):
    # Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.get(BlogPost, post_id)  # returns: either a post or None
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def add_post():
    form = NewPost()
    if request.method == "POST" and form.validate_on_submit():
        title = request.form.get("title")
        subtitle = request.form.get("subtitle")
        author_name = request.form.get("author_name")
        background_image_url = request.form.get("background_image_url")
        body_data = cleanify(
            request.form.get("ckeditor")
        )  # Sanitize the new body element before saving it to the db
        return render_template("index.html")

    return render_template("make-post.html", form=form)


# TODO: edit_post() to change an existing blog post

# TODO: delete_post() to remove a blog post from the database


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
