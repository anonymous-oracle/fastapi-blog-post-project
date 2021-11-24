from fastapi import testclient
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app, base_url="http://localhost:8000")


def test_root():
    res = client.get("/")
    print(res.json())
    assert res.json().get("message") == "Hello World"
    assert res.status_code == 200


def test_create_user():
    res = client.post(
        "/users",
        json={"email": "user2@app.com", "password": "admin123"},
    )
    print(res.text)


def test_get_users():
    res = client.get("/users")
    # print(res.text)
