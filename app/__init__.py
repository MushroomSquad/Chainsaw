from fastapi import FastAPI
from .server import Server
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    server = Server(app)
    await server.on_startup("./app/.env")
    yield
    await server.on_shutdown()


def main(
    _=None,
) -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    return app
