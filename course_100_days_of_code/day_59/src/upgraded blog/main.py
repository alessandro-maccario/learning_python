from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


# Import the npoint.io json blog data
blog_posts = requests.get(
    "https://api.npoint.io/12dbc378eab2f22b5542", auth=("user", "pass")
)
print(blog_posts.json())


if __name__ == "__main__":
    # run the app in debug mode to auto-reload the server
    app.run(debug=True)
