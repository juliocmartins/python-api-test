def test_app_is_created(app):
    assert app.name == 'src'

def test_helthcheck_endpoint(client):
    req = client.get("/helthcheck")
    assert req.status_code == 200

