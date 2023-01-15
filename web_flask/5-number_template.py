#!/usr/bin/python3
"""
Script that starts a web flask application.
"""
from flask import Flask, render_template

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
    Function to display txt on screen.
    """
    return 'HBNB'


@app.route('/c/<custom>', strict_slashes=False)
def path_c_custom(custom):
    """
    Function to display text on screen.
    """
    return 'C %s' % custom.replace('_', ' ')


@app.route('/python', defaults={'custom': 'is cool'}, strict_slashes=False)
@app.route('/python/<path:custom>', strict_slashes=False)
def path_python_custom(custom):
    """
    Function to display text on screen.
    """
    return "Python {}".format(custom.replace('_', ' '))


@app.route('/number/<int:number>', strict_slashes=False)
def path_number_custom(number):
    """
    Function that display custom number on screen.
    """
    return "{} is a number".format(number)


@app.route('/number_template/<int:number>', strict_slashes=False)
def path_number_template(number):
    """
    Function that display custom number on screen.
    """
    return render_template('5-number.html', number=number)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
