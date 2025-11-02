from app import app
from flask import render_template, request, jsonify
from app.models import db, Cafe


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

        return render_template("cafes.html", cafes_data=dict_all_cafe)
