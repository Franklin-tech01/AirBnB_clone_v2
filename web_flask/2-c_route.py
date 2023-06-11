#!/usr/bin/python3
"""
2. C is fun!
Script that starts a Flask web application.
python3 -m web_flask.2-c_route
curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """response text for root route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """response text for /hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """response text"""
    text = text.replace("_", " ")
    return 'C %s' % text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
