from database import client, session


def test_root(client, session):

    res = client.get("/")
    print(res.json())
    assert res.json().get("message") == "Hello World"
    assert res.status_code == 200


def test_create_user(client):
    res = client.post(
        "/users",
        json={"email": "user2@app.com", "password": "admin123"},
    )
    print(res.text)


def test_get_users(client):
    res = client.get("/users")
    print(res.text)
