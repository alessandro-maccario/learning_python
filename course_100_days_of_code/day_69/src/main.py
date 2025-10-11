from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from functools import wraps
from typing import List

# from flask_gravatar import Gravatar
from hashlib import sha256
from urllib.parse import urlencode
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, URL, Email

# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
import os
import nh3
from dotenv import load_dotenv

load_dotenv()  # take environment variables


def gravatar_url(
    email,
    size=100,
    rating="g",
    default="retro",
    force_default=False,
):
    hash_value = sha256(email.lower().encode("utf-8")).hexdigest()
    query_params = urlencode(
        {"d": default, "s": str(size), "r": rating, "f": force_default}
    )
    return f"https://www.gravatar.com/avatar/{hash_value}?{query_params}"


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.jinja_env.filters["gravatar"] = gravatar_url
ckeditor = CKEditor(app)
Bootstrap5(app)


# --- Flask-Login setup --- #
# Instantiate the Login Manager: https://flask-login.readthedocs.io/en/latest/
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


# get current file path for project folder and define location for saving the db
file_path = os.path.abspath(os.getcwd()) + "/src/instance/"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{file_path}/posts.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# This gives you the current_user information
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)


# CONFIGURE TABLES
# Create a User table for all your registered users.
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
    posts: Mapped[List["BlogPost"]] = relationship()
    comments: Mapped[List["Comment"]] = relationship()


# Create a BlogPost table to collect all the blog posts for each users
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    # Establish One-to-Many: one BlogPost → many Comments
    comments: Mapped[List["Comment"]] = relationship(back_populates="parent_post")


class Comment(db.Model):
    __tablename__ = "comments"
    id = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("blog_posts.id"))
    # Establish the "Many-to-One" side (each comment → one BlogPost)
    parent_post: Mapped["BlogPost"] = relationship(back_populates="comments")
    body: Mapped[str] = mapped_column(Text, nullable=False)


with app.app_context():
    db.create_all()

# Define allowed tags & attributes to be inserted in user input text to the database
ALLOWED_TAGS = {"p", "b", "i", "u", "em", "strong", "a", "ul", "ol", "li", "br"}
ALLOWED_ATTRIBUTES = {
    "a": {
        "href",
    },
    "img": {
        "alt",
        "src",
    },
}


# create your own decorator to block users if not admin to edit posts
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_anonymous or not (current_user.id == 1):
            return abort(403)
            # return redirect(url_for("login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


# Use Werkzeug to hash the user's password when creating a new user.
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST" and form.validate_on_submit():
        # save the new user into the database
        new_user = User(
            name=form.name.data,
            email=form.email.data,
            # generate hashed and salted password using Werkzeug
            password=generate_password_hash(
                form.password.data, method="pbkdf2", salt_length=8
            ),
        )

        # check if the email already exists in the database. If it does, then redirect to sign up/register page for the user to try again
        user = db.session.execute(
            db.select(User).where(User.email == new_user.email)
        ).one_or_none()
        # if this returns a user, then the email already exists in database

        if user:  # if a user is found, we want to redirect back to register/signup page so user can try again
            # add a custom message to let the user know that that email address already exists
            flash("Email address already exists, login to enter your account")
            return redirect(url_for("login"))
        else:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("login"))
    return render_template("register.html", form=form)


# Retrieve a user from the database based on their email.
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        # get email value to check if the user already exists in the database
        email = form.email.data
        # check if the email already exists in the database
        user = (
            db.session.execute(
                db.select(User).where(User.email == email)
            ).scalar_one_or_none()
        )  # if this returns a user, then the email already exists in database

        if not user:
            flash("User not found, please register to use our services!")
            return redirect(url_for("register"))

        elif user and check_password_hash(user.password, form.password.data):
            # then log the user in!
            login_user(user)
            flash("Logged in successfully!", "success")
            return redirect(url_for("get_all_posts"))
        else:
            flash("Wrong password, try again!")
            return redirect(url_for("login"))

    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("get_all_posts"))


@app.route("/")
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


# Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
@login_required
def show_post(post_id):
    form = CommentForm()
    requested_post = db.get_or_404(BlogPost, post_id)

    if request.method == "POST" and form.validate_on_submit():
        # save the new user into the database
        new_comment = Comment(
            author_id=current_user.id,
            author=current_user.name,
            post_id=post_id,
            body=nh3.clean(
                form.body.data,
                tags=ALLOWED_TAGS,
                attributes=ALLOWED_ATTRIBUTES,
            ),
        )

        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for("get_all_posts"))

    return render_template("post.html", post=requested_post, form=form)


# Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=nh3.clean(
                form.body.data,
                tags=ALLOWED_TAGS,
                attributes=ALLOWED_ATTRIBUTES,
            ),
            img_url=form.img_url.data,
            author=current_user.name,
            author_id=current_user.id,
            date=date.today().strftime("%B %d, %Y"),
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body,
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user.name
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
