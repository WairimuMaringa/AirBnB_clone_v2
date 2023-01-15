#!/usr/bin/python3
"""
Script that starts a web flask application.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def path():
    """
    Function to display text on screen.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def path_hbnb():
    """
    Function to display txt o screem.
    """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
