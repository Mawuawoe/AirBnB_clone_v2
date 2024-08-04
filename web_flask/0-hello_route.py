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


if __name__ == "__main__":
    """
    Runs the Flask web application on host 0.0.0.0 and port 5000.
    """
    app.run(host="0.0.0.0", port=5000)
