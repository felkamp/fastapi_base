from fastapi import APIRouter, Depends
from src.models.song import Song, SongCreate
from sqlalchemy import select
from src.db.base import get_session

from sqlmodel import Session

router = APIRouter(prefix='/songs', tags=['Song'])


@router.get('', response_model=list[Song])
def get_songs(session: Session = Depends(get_session)):
    result = session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, artist=song.artist, id=song.id) for song in songs]


@router.post("")
def add_song(song: SongCreate, session: Session = Depends(get_session)):
    song = Song(name=song.name, artist=song.artist)
    session.add(song)
    session.commit()
    session.refresh(song)
    return song
