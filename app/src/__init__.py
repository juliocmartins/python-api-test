import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['APP_NAME'] = os.environ.get("APP_NAME")
    app.config['FLASK_APP'] = os.environ.get("FLASK_APP")
    app.config['FLASK_ENV'] = os.environ.get("FLASK_ENV")
    app.config['FLASK_DEBUG'] = os.environ.get("FLASK_DEBUG")


    @app.route('/')
    def index():
        return "Index, nothing here"

    @app.route('/helthcheck')
    def helthcheck():
        return "OK"

    @app.errorhandler(404)
    def page_not_found(e):
        return "<h1>Not Found</h1>Hey, get out of here!!!", 404

    from src import routes
    routes.init_app(app)

    db.init_app(app)
    ma.init_app(app)

    return app