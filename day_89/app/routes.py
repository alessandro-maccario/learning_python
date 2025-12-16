from app import app
from flask import render_template, request, redirect, url_for
from app.models import tasks


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    new_task = request.form.get("todoitem")
    if new_task:
        tasks.append(new_task)
    return redirect(url_for("index"))


# Add a new route to handle task deletion
@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete_task(id):
    # remove the task from the list
    tasks.pop(id - 1)
    return redirect(url_for("index"))
