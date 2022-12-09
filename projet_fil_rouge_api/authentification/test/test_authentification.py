from mainApi import app
from fastapi.testclient import TestClient
from authentification.service.context import SECRET_USERNAME_TEST, SECRET_PASSWORD_TEST

client = TestClient(app)

# Failure test case
def test_login_without_body():
    response = client.post("/login")
    assert response.status_code == 422

# Failure test case
def test_login_bad_credentials():
    response = client.post("/login",headers={"Content-Type":"application/json"},json={"username":"x","password":"x"})
    assert response.status_code == 403

# Success test case
def test_login_success():
    response = client.post("/login",headers={"Content-Type":"application/json"},json={"username":SECRET_USERNAME_TEST,"password":SECRET_PASSWORD_TEST})
    assert response.status_code == 200
    

    