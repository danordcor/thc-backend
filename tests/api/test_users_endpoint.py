from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from app import create_app


@pytest.fixture
def client() -> TestClient:
    return TestClient(create_app("testing"))


def test_create_and_get_user(client):
    created = client.post("/users", json={"name": "Ada", "email": "Ada@Mentoria.dev"})
    assert created.status_code == 201
    body = created.json()
    assert body["email"] == "ada@mentoria.dev"

    fetched = client.get(f"/users/{body['id']}")
    assert fetched.status_code == 200
    assert fetched.json() == body


def test_invalid_payload_returns_422(client):
    response = client.post("/users", json={"name": "", "email": "no"})
    assert response.status_code == 422


def test_extra_fields_return_422(client):
    response = client.post(
        "/users", json={"name": "Ada", "email": "ada@mentoria.dev", "is_admin": True}
    )
    assert response.status_code == 422


def test_duplicate_email_returns_409(client):
    client.post("/users", json={"name": "Ada", "email": "ada@mentoria.dev"})
    response = client.post("/users", json={"name": "Otra", "email": "ada@mentoria.dev"})
    assert response.status_code == 409


def test_unknown_user_returns_404(client):
    assert client.get(f"/users/{uuid4()}").status_code == 404


def test_malformed_id_returns_422(client):
    assert client.get("/users/no-es-uuid").status_code == 422


def test_delete_returns_204(client):
    user = client.post("/users", json={"name": "Ada", "email": "ada@mentoria.dev"}).json()
    assert client.delete(f"/users/{user['id']}").status_code == 204
    assert client.get(f"/users/{user['id']}").status_code == 404
