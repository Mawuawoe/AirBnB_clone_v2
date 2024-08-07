#!/usr/bin/python3
"""
This module starts a simple Flask web application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states():
    """Render state_list html page to display States created"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(self):
    """
    Removes the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == "__main__":
    """
    Runs the Flask web application on host 0.0.0.0 and port 5000.
    """
    app.run(host="0.0.0.0", port=5000)
