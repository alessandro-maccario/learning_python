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
    DateField,
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


# add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def add_post():
    form = NewPost()
    if request.method == "POST" and form.validate_on_submit():
        # save the post into the database
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=str(date.today().strftime("%B %d, %Y")),
            author=form.author_name.data,
            img_url=form.background_image_url.data,
            # Sanitize the new body element before saving it to the db
            body=cleanify(form.body.data),
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=form)


# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    """
    Editing a post.
    NOTE: HTML forms (WTForms included) do not accept PUT, PATCH or DELETE methods.
    So while this would normally be a PUT request (replacing existing data),
    because the request is coming from a HTML form,
    you should accept the edited post as a POST request.

    Parameters
    ----------
        post_id: id of the post to be edited

    """
    requested_post = db.session.get(BlogPost, post_id)
    form = NewPost(obj=requested_post)
    if request.method == "GET":
        # based on the id of the post in the database, call the data already available for ethe specific post
        return render_template("make-post.html", form=form, post_id=requested_post)
    # TODO: need to save the new object!
    else:
        # if the method is post, the user will modify the current fields with new data
        requested_post.title = form.title.data
        requested_post.subtitle = form.subtitle.data
        requested_post.author = form.author_name.data
        requested_post.img_url = form.background_image_url.data
        # Sanitize the new body element before saving it to the db
        requested_post.body = cleanify(form.body.data)

        # save the post into the database
        db.session.add(requested_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))


# delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>", methods=["GET", "DELETE"])
def delete_post(post_id):
    # collect the post to be removed
    removed_post = db.session.get(BlogPost, post_id)

    # save the post into the database
    db.session.delete(removed_post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
