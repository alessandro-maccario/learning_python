from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func
from random import randint
import os


app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# get current file path for project folder and define location for saving the db
file_path = os.path.abspath(os.getcwd()) + "/day_66/src/instance/"
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{file_path}cafes.db"
db = SQLAlchemy(model_class=Base)
# initialize the app with the extension
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=["GET"])
def random_cafe():
    if request.method == "GET":
        # select the number of rows available in the database and select a random number amongst the id values to then select a random cafe
        cafe_number_of_rows = db.session.query(func.count(Cafe.id)).scalar()
        # get a random number between 1 and the maximum amount of rows available in the database table
        random_id = randint(1, cafe_number_of_rows)
        # Now, based on an id number that exists in the db table, select an existent row in the db table

        random_selected_row = db.session.execute(
            db.select(Cafe).where(Cafe.id == random_id)
        ).scalar_one()  # returns: either a Cafe or error if not found
        dict_result = {
            "cafe": {
                "name": random_selected_row.name,
                "map_url": random_selected_row.map_url,
                "img_url": random_selected_row.img_url,
                "location": random_selected_row.location,
                "seats": random_selected_row.seats,
                "has_toilet": random_selected_row.has_toilet,
                "has_wifi": random_selected_row.has_wifi,
                "has_sockets": random_selected_row.has_sockets,
                "can_take_calls": random_selected_row.can_take_calls,
                "coffee_price": random_selected_row.coffee_price.encode(
                    "ascii", "ignore"
                ).decode(),
            }
        }

        return jsonify(data=dict_result)


# HTTP GET - Read Record
@app.route("/all", methods=["GET"])
def fetch_all_cafe():
    if request.method == "GET":
        select_all_cafe = db.session.execute(db.select(Cafe)).scalars().all()
        dict_all_cafe = {
            "cafes": [
                {
                    "name": cafe.name,
                    "map_url": cafe.map_url,
                    "img_url": cafe.img_url,
                    "location": cafe.location,
                    "seats": cafe.seats,
                    "has_toilet": cafe.has_toilet,
                    "has_wifi": cafe.has_wifi,
                    "has_sockets": cafe.has_sockets,
                    "can_take_calls": cafe.can_take_calls,
                    "coffee_price": cafe.coffee_price,
                }
                for cafe in select_all_cafe
            ]
        }

        return jsonify(dict_all_cafe)


@app.route("/search", methods=["GET"])
def search_cafe():
    if request.method == "GET":
        # allow the route to read in the query the location parameter, by doing: search?location=Barbican
        location = request.args.get("location")
        # fetch the cafes available in a specific location defined by the user
        cafes_location = (
            db.session.execute(db.select(Cafe).where(Cafe.location == location))
            .scalars()
            .all()
        )

        dict_all_cafe_with_location = {
            "cafes": [
                {
                    "name": cafe.name,
                    "map_url": cafe.map_url,
                    "img_url": cafe.img_url,
                    "location": cafe.location,
                    "seats": cafe.seats,
                    "has_toilet": cafe.has_toilet,
                    "has_wifi": cafe.has_wifi,
                    "has_sockets": cafe.has_sockets,
                    "can_take_calls": cafe.can_take_calls,
                    "coffee_price": cafe.coffee_price,
                }
                for cafe in cafes_location
            ]
        }

        if len(dict_all_cafe_with_location["cafes"]) > 0:
            return jsonify(dict_all_cafe_with_location)
        else:
            return {"error": {"Not Found": "Sorry, cafe not found!"}}


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_new_cafe():
    return {"response": {"Success": "Successfully added the new cafe!"}}


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_cafe_data(cafe_id):
    # allow the route to read in the query the new coffee price parameter, by doing: update-price/22?new_price=€2.60
    new_price = request.args.get("new_price")

    get_cafe_shop = db.session.get(Cafe, cafe_id)  # returns: either a Cafe or None
    if get_cafe_shop is None:
        return jsonify(
            error={
                "Not Found": "Sorry a cafe with that id was not found in the database."
            }
        ), 404
    else:
        # If found, update the price and commit the change
        get_cafe_shop.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id: int):
    # allow the route to read in the API key to remove a specific entry only if you have the rights to it
    api_key = request.args.get("api-key")

    get_cafe_shop = db.session.get(Cafe, cafe_id)  # returns: either a Cafe or None

    if get_cafe_shop is None:
        return jsonify(
            error={
                "Not Found": "Sorry a cafe with that id was not found in the database."
            }
        ), 404
    elif get_cafe_shop is not None and api_key != "test":
        return jsonify(
            error={"Sorry, you do not have the correct api key to perform this action."}
        )
    else:
        # If found, delete the cafe and commit the change
        db.session.delete(get_cafe_shop)
        db.session.commit()
        return jsonify(response={"success": "Record successfully deleted."}), 200


if __name__ == "__main__":
    app.run(debug=True)
