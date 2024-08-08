#!/usr/bin/python3
"""
a script that starts a Flask web application
it provide a list os state & a list of cities
"""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_1(id=None):
    """
    if id and state, then the html response
    will list the state and associate cities
    """
    states = storage.all(State)
    if id:
        key = '{}.{}'.format('State', id)
        if key in states:
            states = states[key]
        else:
            states = None
    else:
        states = storage.all(State).values()
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
