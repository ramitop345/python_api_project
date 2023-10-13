from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    res = client.get("/")
    assert res.json().get("message") == 'Hello World'

def test_create_user():
    #res = client.post("/users/", json={"eamil": "testemail@yahoo.com", "password": "testpassword"})
    #assert res.status_code == 201
    #assert res.json().get("email") == "testemail@yahoo.com"
    #new_user = schemas.UserOut(**res.json())
    #assert new_user.email == "email"
    pass