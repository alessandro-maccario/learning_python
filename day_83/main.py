### Day 83: Professional Portfolio Project
from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/experience")
def experience_page():
    return render_template("experience.html")


@app.route("/education")
def education_page():
    return render_template("education.html")


@app.route("/skills")
def skills_page():
    return render_template("skills.html")


@app.route("/interests")
def interests_page():
    return render_template("interests.html")


@app.route("/projects")
def projects_page():
    with open("instance/projects.json") as json_file:
        projects_json_data = json.load(json_file)

    return render_template("projects.html", projects=projects_json_data)


@app.route("/certifications")
def certifications_page():
    return render_template("certifications.html")


if __name__ == "__main__":
    app.run(debug=True)
