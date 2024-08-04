#!/usr/bin/python3
"""
This module starts a simple Flask web application.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Displays a simple message 'Hello HBNB!' on the root route.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays a simple message 'HBNB!' for /hbnb
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    handles the text variable on the /c/<text> route.
    Args:
        text (str): The text to be displayed after 'C '
    """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    handles the text variable on the /python/<text> route.
    """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    handles the an int variable.
    """
    return f"{n} is a number"


if __name__ == "__main__":
    """
    Runs the Flask web application on host 0.0.0.0 and port 5000.
    """
    app.run(host="0.0.0.0", port=5000)
