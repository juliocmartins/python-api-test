from src import app, ma
from src.models import *

class PokemonsTypesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PokemonsTypes

class PokemonsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pokemons

    # types = ma.Nested(PokemonsTypesSchema(only=("poke_type",)), many=True)
    types = ma.Pluck(PokemonsTypesSchema,"poke_type", many=True)