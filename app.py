"""Flask app for Cupcakes"""

import os

from flask import Flask, request, redirect, render_template, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Cupcake

# from forms import

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///cupcakes")

app.config['SQLALCHEMY_ECHO']=True

connect_db(app)

@app.get('/api/cupcakes')
def get_cupcakes():
    """ get data about all cupcakes """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.get('/api/cupcakes/<int:cupcake_id>')
def get_single_cupcake(cupcake_id):
    """ get data about specific cupcakes """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

