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
from wtforms.validators import DataRequired, URL
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
Bootstrap5(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


# get current file path for project folder and define location for saving the db
file_path = os.path.abspath(os.getcwd()) + "/day_68/src/instance/"
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{file_path}users.db"
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
    email = StringField(label="Email", validators=[DataRequired()])
    password = StringField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Sign me up!")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = NewUser()
    if request.method == "POST" and form.validate_on_submit():
        # save the post into the database
        new_user = User(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data,
        )
        # db.session.add(new_user)
        # db.session.commit()
        return redirect(url_for("home"))
    return render_template("register.html", form=form)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/secrets")
def secrets():
    return render_template("secrets.html")


@app.route("/logout")
def logout():
    pass


@app.route("/download")
def download():
    pass


if __name__ == "__main__":
    app.run(debug=True)
