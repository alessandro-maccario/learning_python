from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os
import requests
from dotenv import load_dotenv

# load .env variables
load_dotenv()

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


# configuration of mail
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
mail = Mail(app)


@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone_number = request.form["phone"]
        message = request.form["message"]
        print("Username:", name)
        print("Password:", email)
        print("Password:", phone_number)
        print("Password:", message)

        msg = Message(
            "Hello Friend...",
            sender=email,  # email of the sende
            recipients=["bebinih317@anysilo.com"],  #
        )
        msg.body = "Hello Flask message sent from Flask-Mail"
        mail.send(msg)
        successful_message_sent = "Message sent!"
    # return f"<h1>Successfully sent your message</h1>"
    return render_template(
        "contact.html",
        success_message=successful_message_sent,
    )


# message object mapped to a particular URL ‘/’
@app.route("/")
def index():
    msg = Message(
        "Hello", sender="yourId@gmail.com", recipients=["receiver’sid@gmail.com"]
    )
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
