#!/usr/bin/python3
"""
3. Python is cool!
Script that starts a Flask web application.
python3 -m web_flask.3-python_route
curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """response text for the /c/<text> route"""
    text = text.replace("_", " ")
    return 'C %s' % text


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """response text"""
    text = text.replace("_", " ")
    return 'Python %s' % text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
