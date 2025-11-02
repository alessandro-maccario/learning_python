from app import app
from flask import render_template
import os

# get current file path for project folder and define location for saving the db
file_path = os.path.abspath(os.getcwd()) + "/day_66/src/instance/"
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{file_path}cafes.db"
db = SQLAlchemy(model_class=Base)
# initialize the app with the extension
db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


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
