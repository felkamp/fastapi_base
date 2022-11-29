import pytest
from fastapi.testclient import TestClient

from sqlmodel import SQLModel, create_engine, Session
from src.main import app

DATABASE_URL = 'postgresql+psycopg2://user:pass@db:5432/postgres'
engine = create_engine(DATABASE_URL)
schemas = ['test']


@pytest.fixture(scope="function")
def client():
    yield TestClient(app)


@pytest.fixture(scope="session", autouse=True)
def init_db():
    SQLModel.metadata.drop_all(bind=engine)
    with Session(engine) as session:
        for schema in schemas:
            session.execute(f"create schema if not exists {schema}")
        session.commit()
    SQLModel.metadata.create_all(bind=engine)
    yield
    SQLModel.metadata.drop_all(bind=engine)
