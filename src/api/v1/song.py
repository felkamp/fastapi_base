from fastapi import APIRouter, Depends
from src.models.song import Song, SongCreate
from src.db.base import get_async_session
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(prefix='/songs', tags=['Song'])


@router.get('', response_model=list[Song])
async def get_songs(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, artist=song.artist, id=song.id) for song in songs]


@router.post("")
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_async_session)):
    song = Song(name=song.name, artist=song.artist)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song
