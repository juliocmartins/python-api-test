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