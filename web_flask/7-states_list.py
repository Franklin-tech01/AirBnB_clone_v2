#!/usr/bin/python3
"""script that starts a Flask web application."""

from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """response text for the root route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """response text for the /hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """response text for the the /c/<text> route"""
    text = text.replace("_", " ")
    return 'C %s' % text


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """response text for the /python route, with a default text
    of 'is cool', or the expansion of <text>"""
    text = text.replace("_", " ")
    return 'Python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def is_n(n):
    """response text for the /number/<n> route,
    only if n is an int"""
    if type(n) == int:
        return '%s is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_num(n):
    """response template for the /number_template/<n> route,
    expanding route"""
    if type(n) == int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """response template for the /number_odd_or_even/<n>
    route, display if the number is odd or even"""
    if type(n) == int:
        return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """displays a HTML page of state objects present in DBstorage
    message on page changes depending on value passed"""
    return render_template('7-states_list.html', states=storage.all("State"))


@app.teardown_appcontext
def teardown(err):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
