#!/usr/bin/python3
"""
1. HBNB
Script that starts a Flask web application.
python3 -m web_flask.1-hbnb_route
curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """response text for the root route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """response text for the /hbnb route"""
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
