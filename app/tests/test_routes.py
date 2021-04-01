import json

def test_list_pokemons(client):
    req = client.get("/pokemons")
    assert req.status_code == 200

def test_get_pokemon(client):
    req = client.get("/pokemons/1")
    assert req.status_code == 200

def test_get_missing_pokemon(client):
    req = client.get("/pokemons/99999999")
    assert req.status_code == 404

def test_list_trainers(client):
    req = client.get("/trainers")
    assert req.status_code == 200

def test_get_trainer(client):
    req = client.get("/trainers/1")
    assert req.status_code == 200

def test_get_missing_trainer(client):
    req = client.get("/trainers/10000")
    assert req.status_code == 404

def test_post_trainers(client):
    req = client.post("/trainers", json=dict(name="Ashtest"))
    assert req.status_code == 201

def test_post_team(client):
    req = client.post("/trainers/4/team", json=dict(name="Teamtest", pokemons=[1,4,7]))
    assert req.status_code == 201

def test_post_invalid_team_name(client):
    req = client.post("/trainers/4/team", json=dict(name="Team", pokemons=[1,4,7]))
    assert req.status_code == 400

def test_post_team_too_big(client):
    req = client.post("/trainers/4/team", json=dict(name="Team", pokemons=[1,4,7,10,14,21,55]))
    assert req.status_code == 400