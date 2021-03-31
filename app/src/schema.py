from src import ma
from src.models import *

class PokemonsTypesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PokemonsTypes

class PokemonsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pokemons

    # types = ma.Nested(PokemonsTypesSchema(only=("poke_type",)), many=True)
    types = ma.Pluck(PokemonsTypesSchema,"poke_type", many=True)

class TeamPokemonsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TeamPokemons

class TeamsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Teams

    # pokemons = ma.Nested(TeamPokemonsSchema,many=True)

class TrainersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trainers

    # team = ma.Pluck(TeamsSchema,"name")
    team = ma.Nested(TeamsSchema)



