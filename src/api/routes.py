from fastapi import APIRouter

from src.api.v1 import smoke
from src.api.v1 import song

api_router = APIRouter()
api_router.include_router(smoke.router)
api_router.include_router(song.router)
