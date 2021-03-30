from src.controllers.pokemons import pokemons_controller
from src.controllers.teams import teams_controller
from src.controllers.trainers import trainers_controller
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

#trainer
@app.route("/trainers")
def list_trainers():
    return trainers_controller.list_trainers()

@app.route("/trainers/<int:id>/")
def get_trainer(id):
    return trainers_controller.get_trainer(id)

@app.route("/trainers", methods=['POST'])
def save_trainer():
    return trainers_controller.save_trainer(request.json)

@app.route("/trainers/<int:id>", methods=['PUT'])
def edit_trainer(id):
    trainer = request.json
    return trainers_controller.edit_trainer(id, trainer)

@app.route("/trainers/<int:id>", methods=['DELETE'])
def delete_trainer(id):
    return trainers_controller.delete_trainer(id)

#team
@app.route("/trainers/<int:id>/team", methods=['POST'])
def save_team(id):
    team = request.json
    return teams_controller.save_team(id,team)

@app.route("/trainers/<int:id>/team", methods=['PUT'])
def edit_team(id):
    team = request.json
    return teams_controller.edit_team(id, team)

@app.route("/trainers/<int:id>/team", methods=['DELETE'])
def delete_team(id):
    return teams_controller.delete_team(id)
