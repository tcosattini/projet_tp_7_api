from mainApi import app
from fastapi.testclient import TestClient
from authentification.service.context import SECRET_TOKEN_TEST,SECRET_USERNAME_TEST
client = TestClient(app)

# Failure test case GET request without bearer token
def test_get_all_clients_without_token():
    response = client.get("/client")
    assert response.status_code == 403


# Success test case
def test_get_all_clients_success():
    response = client.get("/client",headers={"Authorization":SECRET_TOKEN_TEST})
    assert response.status_code == 200


# Failure test case 
def test_post_client_validation_error():
    response = client.post("/client",headers={"Authorization":SECRET_TOKEN_TEST},json={
	"username":"x",
	"is_superuser":"false",
	"role":["IS_GS"]
})
    assert response.status_code == 422

# Failure test case 
def test_post_client_already_registred_error():
    response = client.post("/client",headers={"Authorization":SECRET_TOKEN_TEST},json={
	"username": SECRET_USERNAME_TEST,
  "password":"xxxx",
	"is_superuser":"false",
	"role":["IS_GS"]
})
    assert response.status_code == 422




