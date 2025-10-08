from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    send_from_directory,
)
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.security import safe_join
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)
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
from wtforms.validators import DataRequired, URL, Email
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables

app = Flask(__name__, static_folder="static")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
Bootstrap5(app)
# Instantiate the Login Manager: https://flask-login.readthedocs.io/en/latest/
# login_manager = LoginManager()
# login_manager.init_app(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


# get current file path for project folder and define location for saving the db
file_path = os.path.abspath(os.getcwd()) + "/day_68/src/instance/"
static_filepath = os.path.abspath(os.getcwd()) + "/day_68/src/static/files/"
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{file_path}users.db"
app.config["FILE_2_DOWNLOAD"] = f"{static_filepath}"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE IN DB
class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


# Define the New Post Form
class NewUser(FlaskForm):
    name = StringField(
        label="Name",
        validators=[
            DataRequired(),
        ],
    )
    email = EmailField(
        label="Email",
        validators=[DataRequired(), Email()],
    )
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Sign me up!")


# Define the login form
class NewLogin(FlaskForm):
    email = EmailField(
        label="Email",
        validators=[DataRequired(), Email()],
    )
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Let me in.")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = NewUser()
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
        user = User.query.filter_by(
            email=new_user.email
        ).first()  # if this returns a user, then the email already exists in database

        if user:  # if a user is found, we want to redirect back to register/signup page so user can try again
            # add a custom message to let the user know that that email address already exists
            flash("Email address already exists, login to enter your account")
            return redirect(url_for("login"))
        else:
            db.session.add(new_user)
            db.session.commit()
            return render_template("secrets.html", name=form.name.data)
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = NewLogin()
    form_new_user = NewUser()

    if request.method == "POST" and form.validate_on_submit():
        # get email value to check if the user already exists in the database
        email = form.email.data
        # check if the email already exists in the database
        user = User.query.filter_by(
            email=email
        ).first()  # if this returns a user, then the email already exists in database

        if user:
            # check if the password is correct
            password = check_password_hash(user.password, form.password.data)
            if password:  # if true = correct password match
                return render_template("secrets.html", name=user.name)
            else:
                flash("Wrong password, try again!")
                return render_template("login.html", form=form)
        else:
            flash("User not found, please register to use our services!")
            return render_template("register.html", form=form_new_user)
    return render_template("login.html", form=form)


@app.route("/secrets")
def secrets():
    return render_template("secrets.html")


@app.route("/logout")
def logout():
    pass


@app.route("/download/<path:name>")
def download(name):
    return send_from_directory(app.static_folder, name, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
