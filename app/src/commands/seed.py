import os, json
from flask import current_app
from flask_script import Command

from src import create_app, db
from src.models import *

dir_path = os.path.join(os.path.dirname(os.path.dirname(__file__)))

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

class Seed(Command):
    """ Seed the database."""
    def run(self):
        reset_db()
        seed_pokemons()
        seed_trainers()

def reset_db():
    db.drop_all()
    db.create_all()

def seed_pokemons():
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

def seed_trainers():
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

def drop_all():
    print("Dropping tables...")
    db.drop_all()