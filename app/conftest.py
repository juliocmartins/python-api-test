import os, pytest
from src import create_app, db
from src.models import *
from manage import drop_all

test_app = create_app()
test_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test.db')

test_app.app_context().push()

from src.commands.seed import seed_pokemons, seed_trainers, reset_db
reset_db()
seed_pokemons()
seed_trainers()

@pytest.fixture(scope="module")
def app():
    def teardown():
        drop_all()

    """ Instace of main flask app"""
    return test_app

# @pytest.fixture(scope='module')
# def init_database(app):
    # Create the database and the database table
    # db.create_all()

    # t = Trainers(name='Julio')
    # db.session.add(t)

    # db.session.commit()
    # db.drop_all()