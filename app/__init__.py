from fastapi import FastAPI

from contextlib import asynccontextmanager

from collections.abc import AsyncIterator

from .server import Server


@asynccontextmanager
async def lifespan(
    app: FastAPI,
) -> AsyncIterator:
    server: Server = Server(app)
    await server.on_startup("./app/.env")
    yield
    await server.on_shutdown()


def main(
    _=None,
) -> FastAPI:
    app: FastAPI = FastAPI(lifespan=lifespan)
    return app
