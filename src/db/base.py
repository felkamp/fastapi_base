from src.models.song import Song
from sqlmodel import create_engine, SQLModel, Session
from src.core.config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL, echo=settings.DEBUG)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
