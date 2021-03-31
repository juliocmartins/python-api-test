from src import app, db, jsonify
from src.models import Pokemons,PokemonsTypes
from src.schema import PokemonsSchema

import json

class PokemonsController():
    def __init__(self):
        pass

    def list_pokemons(self, filters):
        schema = PokemonsSchema()
        q = Pokemons.query
        
        if('name' in filters):
            q = q.filter_by(name=filters['name'])
        
        if('type' in filters):
            q = q.join(PokemonsTypes).filter(PokemonsTypes.poke_type == filters['type'])
            
        monsters = q.all()
        return schema.dumps(monsters, many=True), 200

    def get_pokemons(self, id):
        schema = PokemonsSchema()
        monster = Pokemons.query.filter_by(id=id).first()
        
        return schema.dumps(monster), 200

pokemons_controller = PokemonsController()