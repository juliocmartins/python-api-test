from src.controllers.pokemons import pokemons_controller
from src import app, request

# pokemons
@app.route("/pokemons")
def list_pokemons():
    filters = {}
    if 'type' in request.args:
        filters['type'] = request.args.get('type')

    if 'name' in request.args:
        filters['name'] = request.args.get('name')
    
    return pokemons_controller.list_pokemons(filters)

@app.route("/pokemons/<int:id>")
def get_pokemons(id):
    return pokemons_controller.get_pokemons(id)