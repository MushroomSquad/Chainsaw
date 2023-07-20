from fastapi import FastAPI
from .server import Server


def main(
    _=None,
) -> FastAPI:
    app = FastAPI()
    server = Server(app)

    @app.on_event("startup")
    async def on_startup_app():
        await server.on_startup("./app/.env")

    @app.on_event("shutdown")
    async def on_shutdown_app():
        await server.on_shutdown()

    return app
