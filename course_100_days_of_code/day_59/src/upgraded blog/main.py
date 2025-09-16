from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    # Import the npoint.io json blog data
    blog_url = "https://api.npoint.io/12dbc378eab2f22b5542"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


# Route to reach the post based on the ID of the post
@app.route("/post/<int:id>")
def get_blog(id: int):
    blog_url = "https://api.npoint.io/12dbc378eab2f22b5542"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("post.html", posts=all_posts, post_id=id)


# missing href links for each post!


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


if __name__ == "__main__":
    # run the app in debug mode to auto-reload the server
    app.run(debug=True)
