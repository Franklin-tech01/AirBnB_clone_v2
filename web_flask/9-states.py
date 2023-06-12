#!/usr/bin/python3
# """script that starts a Flask web application"""

# from models import *
# from flask import Flask, render_template
# app = Flask(__name__)


# @app.route('/', strict_slashes=False)
# def hello():
#     """response text for the root route"""
#     return 'Hello HBNB!'


# @app.route('/hbnb', strict_slashes=False)
# def hbnb():
#     """response text for the /hbnb route"""
#     return 'HBNB'


# @app.route('/c/<text>', strict_slashes=False)
# def c_text(text):
#     """response text for the the /c/<text> route"""
#     text = text.replace("_", " ")
#     return 'C %s' % text


# @app.route('/python/', strict_slashes=False)
# @app.route('/python/<text>', strict_slashes=False)
# def python_text(text="is cool"):
#     """response text for the /python route, with a default text
#     of 'is cool', or the expansion of <text>"""
#     text = text.replace("_", " ")
#     return 'Python %s' % text


# @app.route('/number/<int:n>', strict_slashes=False)
# def is_n(n):
#     """response text for the /number/<n> route,
#     only if n is an int"""
#     if type(n) == int:
#         return '%s is a number' % n


# @app.route('/number_template/<int:n>', strict_slashes=False)
# def template_num(n):
#     """response template for the /number_template/<n> route,
#     expanding route"""
#     if type(n) == int:
#         return render_template('5-number.html', n=n)


# @app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
# def number_odd_or_even(n):
#     """response template for the /number_odd_or_even/<n>
#     route, display if the number is odd or even"""
#     if type(n) == int:
#         return render_template('6-number_odd_or_even.html', n=n)


# @app.route('/states_list', strict_slashes=False)
# def states_list():
#     """displays a HTML page of state objects present in DBstorage
#     message on page changes depending on value passed"""
#     return render_template('7-states_list.html', states=storage.all("State"))


# @app.route('/cities_by_states', strict_slashes=False)
# def cities_by_states():
#     """displays a HTML page of city objects
#     in a nested list of state objects present in DBstorage
#     message on page changes depending on value passed"""
#     return render_template(
#         '8-cities_by_state.html', states=storage.all("State"))


# @app.route('/states', strict_slashes=False)
# @app.route('/states/<id>', strict_slashes=False)
# def states_1(id=None):
#     """Returns a rendered html template:
#     if id is given, list the cities of that State
#     else, list all States
#     """

#     states = storage.all('State')
#     if id:
#         key = '{}.{}'.format('State', id)
#         if key in states:
#             states = states[key]
#         else:
#             states = None
#     else:
#         states = storage.all('State').values()
#     return render_template('9-states.html', states=states, id=id)


# @app.teardown_appcontext
# def teardown(err):
#     storage.close()


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port='5000')
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def display_states():
    states = storage.all("State")
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def display_cities(id):
    states = storage.all("State")
    state = states.get(id)
    if state:
        cities = state.cities if hasattr(state, 'cities') else state.cities()
        sorted_cities = sorted(cities, key=lambda x: x.name)
        return render_template('9-states.html', state=state, cities=sorted_cities)
    return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown_session(exception=None):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
