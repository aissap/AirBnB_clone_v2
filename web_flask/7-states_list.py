#!/usr/bin/python3
"""start a Flask web application"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(_name_)


@app.route("/states_list", strict_slashes=False)
def states_list():
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    storage.close()


if _name_ == "_main_":
    app.run(host='0.0.0.0', port=5000)
