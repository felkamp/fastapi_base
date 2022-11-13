import asyncio
from fastapi import APIRouter

router = APIRouter(prefix='/smoke', tags=['Smoke'])


@router.get('')
async def smoke():
    await asyncio.sleep(1)
    return {'smoke'}
