from src import db
from src.models import Trainers,Teams

def test_save_trainer():
    t = Trainers(name="Ash_Test")
    t.save()

    assert type(t.id) is int 
    assert t.id > 0

def test_save_team():
    t = Trainers(name="Ash_Test")
    t.save()

    tm = Teams(name="Team_Test", trainer_id=t.id)
    tm.save()
    assert type(tm.id) is int 
    assert tm.id > 0
