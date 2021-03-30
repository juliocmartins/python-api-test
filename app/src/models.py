from src import app, db

class Pokemons(db.Model):
    __tablename__ = 'pokemons'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    xp = db.Column(db.Integer)
    image = db.Column(db.String(255))
    types = db.relationship("PokemonsTypes",backref="types", lazy="joined")

    def __init__(self,id,name,height,weight,xp,image):
        self.id = id
        self.name = name
        self.height = height
        self.weight = weight
        self.xp = xp
        self.image = image

    def save(self):
        db.session.add(self)
        db.session.commit()

class PokemonsTypes(db.Model):
    __tablename__ = 'pokemons_types'

    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemons.id'))
    poke_type = db.Column(db.String(30))
    

    def __init__(self,pokemon_id,poke_type):
        self.pokemon_id = pokemon_id
        self.poke_type = poke_type

    def save(self):
        db.session.add(self)
        db.session.commit()

class Trainers(db.Model):
    __tablename__ = 'trainers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    team = db.relationship("Teams", uselist=False, backref="team")

    def __init__(self,name):
        self.name = name
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Teams(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.id'))
    name = db.Column(db.String(50))
    pokemons = db.relationship("TeamPokemons",backref="pokemons")

    def __init__(self,name,trainer_id):
        self.name = name
        self.trainer_id = trainer_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class TeamPokemons(db.Model):
    __tablename__ = 'teams_pokemons'

    def __init__(self,team_id,pokemon_id):
        self.team_id = team_id
        self.pokemon_id = pokemon_id

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemons.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()