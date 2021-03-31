import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['APP_NAME'] = os.environ.get("APP_NAME")
app.config['FLASK_APP'] = os.environ.get("FLASK_APP")
app.config['FLASK_ENV'] = os.environ.get("FLASK_ENV")
app.config['FLASK_DEBUG'] = os.environ.get("FLASK_DEBUG")

db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.route('/helthcheck')
def helthcheck():
    return "OK"

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Not Found</h1>Hey, get out of here!!!"

from src import routes
from src.models import *
from src.schema import *

db.create_all()