import os, json
from flask import Flask
from flask_script import Manager
from src import app, db
from src.models import *

dir_path = os.path.dirname(os.path.realpath(__file__))

manager = Manager(app)


trainers = [
        {
            'name' : "Ash",
            'team' : [1,4,7,10,16,25]
        },
        {
            'name' : "Brock",
            'team' : [74,95]
        },
        {
            'name' : "Mist",
            'team' : [54, 118, 120]
        }
]

@manager.command
def seed():
    db.drop_all()
    db.create_all()
    with open(dir_path+'/inc/pokemon.json') as json_file:
        pokemons = json.load(json_file)
        types_list = []
        for pokemon in pokemons['pokemon']:
            poke = Pokemons( 
                 id=pokemon['id'],
                 name=pokemon['name'],
                 height=pokemon['height'],
                 weight=pokemon['weight'],
                 xp=pokemon['xp'],
                 image=pokemon['image']
            )
            types_list.append({'id' : pokemon['id'], 'types' :  pokemon['types']})
            poke.save()

        for types in types_list:
            for t in types['types']:
                pt = PokemonsTypes(
                    pokemon_id = types['id'],
                    poke_type=t
                )
                pt.save()

    print('Pokemons Imported!!')

    for trainer in trainers:
        train = Trainers(name=trainer['name'])
        train.save()

        team = Teams(
            name="Noob Team",
            trainer_id=train.id
        )
        team.save()

        for poke_id in trainer['team']:
            poke_team = TeamPokemons(
                team_id=team.id,
                pokemon_id=poke_id
            )
            poke_team.save()

    print('Trainers Imported!!')


@manager.command
def init_db():
    print("Creating all resources.")
    db.create_all()


@manager.command
def drop_all():
    if input("Are you sure you want to drop all tables? (y/N)\n").lower() == "y":
        print("Dropping tables...")
        db.drop_all()


if __name__ == "__main__":
    manager.run()