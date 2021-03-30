from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import *

app = Flask(__name__)

app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_APP'] = "run.py"

db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.route('/helthcheck')
def helthcheck():
    return "OK"

from src import routes
from src.models import *
from src.schema import *

db.create_all()