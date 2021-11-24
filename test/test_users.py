from fastapi.testclient import TestClient
from app.main import app
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.database import get_db, Base
import pytest

# test database
DATABASE_URL = f"""postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"""

engine_ = create_engine(DATABASE_URL)


def override_get_db():
    db = Session(autocommit=False, autoflush=False, bind=engine_)
    try:
        yield db
    finally:
        db.close()


# override get_db with override_get_db
app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    # # drops any existing tables
    # Base.metadata.drop_all(bind=engine_)

    # run code before yield
    Base.metadata.create_all(bind=engine_)

    yield TestClient(app)

    # # run code after yield
    # Base.metadata.drop_all(bind=engine_)


def test_root(client: TestClient):
    res = client.get("/")
    print(res.json())
    assert res.json().get("message") == "Hello World"
    assert res.status_code == 200


def test_create_user(client: TestClient):
    res = client.post(
        "/users",
        json={"email": "user2@app.com", "password": "admin123"},
    )
    print(res.text)


def test_get_users(client: TestClient):
    res = client.get("/users")
    print(res.text)
