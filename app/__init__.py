from fastapi import FastAPI
from .server import Server


def main(
    _=None,
) -> FastAPI:
    app = FastAPI()

    return Server(app).on_startup("./app/.env")
