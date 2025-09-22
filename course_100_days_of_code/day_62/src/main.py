from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location_url = StringField("URL", validators=[DataRequired(), URL()])
    opening_time = StringField("Opening Time", validators=[DataRequired()])
    closing_time = StringField("Closing Time", validators=[DataRequired()])
    coffee_rating = SelectField(
        "Coffee Rating",
        choices=[("1", "☕"), ("2", "☕☕"), ("3", "☕☕☕")],
        validators=[DataRequired()],
    )
    wifi_rating = SelectField(
        "Wifi Rating",
        choices=[("1", "🛜"), ("2", "🛜🛜"), ("3", "🛜🛜🛜")],
        validators=[DataRequired()],
    )
    power_outlet_rating = SelectField(
        "Power Outlet Rating",
        choices=[("1", "🔌"), ("2", "🔌🔌"), ("3", "🔌🔌🔌")],
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add")
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("day_62/src/cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        next(csv_data, None)  # skip the headers
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
