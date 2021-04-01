from flask import jsonify
from src.models import Pokemons,PokemonsTypes
from src.schema import PokemonsSchema

import json

class PokemonsController():
    def __init__(self):
        pass

    def list_pokemons(self, filters):
        schema = PokemonsSchema()
        q = Pokemons.query
        
        try:
            if('name' in filters):
                q = q.filter_by(name=filters['name'])
            
            if('type' in filters):
                q = q.join(PokemonsTypes).filter(PokemonsTypes.poke_type == filters['type'])
                
            monsters = q.all()
        except Exception as e:
            print(e)
            return jsonify({"message":"error"}), 500

        return schema.dumps(monsters, many=True), 200

    def get_pokemons(self, id):
        try:
            schema = PokemonsSchema()
            monster = Pokemons.query.filter_by(id=id).first()

            if not monster:
                return jsonify({"message":"This one was not caught"}), 404

        except Exception as e:
            print(e)
            return jsonify({"message":"error"}), 500

        
        return schema.dumps(monster), 200

pokemons_controller = PokemonsController()