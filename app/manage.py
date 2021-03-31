from flask import Flask
from flask_script import Command, Manager
from src import create_app, db
from src.commands.seed import Seed

app = create_app()
manager = Manager(app)
manager.add_command('seed', Seed())

@manager.command
def init_db():
    print("Creating all resources.")
    db.create_all()


@manager.command
def drop_all():
    # if input("Are you sure you want to drop all tables? (y/N)\n").lower() == "y":
    print("Dropping tables...")
    db.drop_all()


if __name__ == "__main__":
    manager.run()