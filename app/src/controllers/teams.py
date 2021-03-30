from flask import Flask, jsonify
from src.models import Teams,TeamPokemons
from src.schema import *
import json

class TeamsController():
    def __init__(self):
        pass

    def save_team(self, tid,team):
        prev_team = Teams.query.filter_by(trainer_id=tid).first()

        if prev_team:
            return jsonify({"message":"You already have a team"}), 400

        if not team['pokemons']:
            return jsonify({"message":"Missing pokemons"}), 400
        elif len(team['pokemons']) > 6:
            return jsonify({"message":"Too much monsters!"}), 400

        try:
            new_tean = Teams(name=team["name"],trainer_id=tid)
            new_tean.save()

            for poke_id in team["pokemons"]:
                tpoke = TeamPokemons(team_id=new_tean.id,pokemon_id=poke_id)
                tpoke.save()

        except Exception as e:
            print(e)
            return jsonify({"message":"error"}), 500
        
        return jsonify({"message":"Team created!"}), 201


    def edit_team(self, tid, team):
        prev_team = Teams.query.filter_by(trainer_id=tid).first()

        if not prev_team:
            return jsonify({"message":"Team not found"}), 404

        if not team['pokemons']:
            return jsonify({"message":"Missing pokemons"}), 400
        elif len(team['pokemons']) > 6:
            return jsonify({"message":"Too much monsters!"}), 400

        try:
            prev_team.name = team["name"]
            prev_team.trainer_id = tid
            prev_team.save()

            team_pokes = TeamPokemons.query.filter_by(team_id=prev_team.id).delete()

            for poke_id in team["pokemons"]:
                tpoke = TeamPokemons(team_id=prev_team.id,pokemon_id=poke_id)
                tpoke.save()

        except Exception as e:
            print(e)
            return jsonify({"message":"error"}), 500
        
        return jsonify({"message":"Team updated!"}), 200

    def delete_team(self, uid):
        team = Teams.query.filter_by(trainer_id=uid).first()

        if not team:
            return jsonify({"message":"not_found"}), 404

        try:
            team_pokes = TeamPokemons.query.filter_by(team_id=team.id).delete()
            team.delete()

        except Exception as e:
            print(e)
            return jsonify({"message":"error"}), 500

        schema = TeamsSchema()
        return schema.dumps(team), 200


teams_controller = TeamsController()