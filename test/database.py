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


# override get_db with override_get_db


@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine_)
    Base.metadata.create_all(bind=engine_)
    db = Session(autocommit=False, autoflush=False, bind=engine_)
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session):
    # # # drops any existing tables
    # Base.metadata.drop_all(bind=engine_)

    # # run code before yield
    # Base.metadata.create_all(bind=engine_)

    def override_get_db():
        db = Session(autocommit=False, autoflush=False, bind=engine_)
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

    # # run code after yield
    # Base.metadata.drop_all(bind=engine_)
