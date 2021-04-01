from flask import jsonify
from src.models import Trainers,Teams,TeamPokemons
from src.schema import TrainersSchema
import json

#trainer
class TrainersController():
    def __init__(self):
        pass

    def list_trainers(self):
        trainers = Trainers.query.all()
        
        schema = TrainersSchema(many=True)
        return schema.dumps(trainers), 200

    def get_trainer(self, uid):
        trainer = Trainers.query.filter_by(id = uid).first()

        if not trainer:
            return jsonify({"message":"not_found"}), 404
        
        schema = TrainersSchema()
        return schema.dumps(trainer), 200

    def save_trainer(self, trainer):
        try:
            trainer = Trainers(
                name=trainer['name']
            )
            trainer.save()

            schema = TrainersSchema()
        except Exception as e:
            print(e)
            return jsonify({"message":"error"}), 500

        return schema.dumps(trainer), 201

    def edit_trainer(self, uid, update):
        trainer = Trainers.query.filter_by(id=uid).first()

        if not trainer:
            return jsonify({"message":"not_found"}), 404

        try:
            trainer.name = update["name"]
            trainer.save()
        except:
            return jsonify({"message":"error"}), 500

        schema = TrainersSchema()
        return schema.dumps(trainer), 200


    def delete_trainer(self, uid):
        trainer = Trainers.query.filter_by(id=uid).first()

        if not trainer:
            return jsonify({"message":"not_found"}), 404

        try:
            trainer.delete()
        except:
            return jsonify({"message":"error"}), 500

        schema = TrainersSchema()
        return schema.dumps(trainer), 200

trainers_controller = TrainersController()