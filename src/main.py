from fastapi import FastAPI

from src.db.base import init_db
from src.api.routes import api_router


async def on_startup():
    app.router.include_router(api_router, prefix='/api/v1')
    await init_db()


app = FastAPI(
    title='Base fastapi app',
    version='0.0.1',
    docs_url='/docs',
    openapi_url='/openapi',
    on_startup=[on_startup],
)
