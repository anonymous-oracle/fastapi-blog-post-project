from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from .config import settings


DATABASE_URL = f"""postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"""

engine_ = create_engine(DATABASE_URL)

Base = declarative_base()


def get_db():
    db = Session(autocommit=False, autoflush=False, bind=engine_)
    try:
        yield db
    finally:
        db.close()
