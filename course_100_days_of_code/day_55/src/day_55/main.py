# Day 55: Advanced Decorators, Rendering HTML, Parsing URLs and Flask Debugging

from flask import Flask

app = Flask(__name__)


# decorator factory to stay DRY
# In here:
# 1. html_tag("b") → returns a decorator (decorator)
# 2. decorator → takes the function (hello) and returns the wrapped version
# 3. The wrapper executes the function and applies the HTML tag


def html_tag(tag):  # this gives you the possibility to parametrized the decorator
    def decorator(function):  # it takes a function as an input
        def wrapper():  # this trigger the actual function that you will call inside
            return f"<{tag}>{function()}</{tag}>"  # this controls the calling of the function passed in

        return wrapper

    return decorator


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
@html_tag("b")
@html_tag("em")
@html_tag("u")
def bye():
    return "Bye!"


if __name__ == "__main__":
    # run the app in debug mode to auto-reload the server
    app.run(debug=True)
