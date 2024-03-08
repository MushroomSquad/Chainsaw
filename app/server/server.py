from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from dotenv import dotenv_values
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware


from .database import Data_Base
from .routers import register_routes
from .models import DB_Config, Crypt_Config, Config

origins = [
    "*",
]


class Server:
    def __init__(
        self,
        app: FastAPI,
    ) -> None:
        self._app: FastAPI = app

    async def load_config(
        self,
        path: str,
    ) -> Config:
        env: dict = dotenv_values(path)
        return Config(
            db=DB_Config(
                dialect=env["DIALECT"],
                driver=env["DB_DRIVER"],
                host=env["DB_HOST"],
                password=env["DB_PASS"],
                user=env["DB_USER"],
                database=env["DB_NAME"],
            ),
            crypt=Crypt_Config(
                SECRET_KEY=env["SECRET_KEY"],
                ALGORITHM=env["ALGORITHM"],
                ACCESS_TOKEN_EXPIRE_MINUTS=env["ACCESS_TOKEN_EXPIRE_MINUTS"],
                oauth2_scheme=OAuth2PasswordBearer(tokenUrl=env["tokenUrl"]),
                pwd_context=CryptContext(
                    schemes=env["schemes"],
                    deprecated=env["deprecated"],
                ),
            ),
        )

    async def register_cors(
        self,
    ):
        self._app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    async def on_startup(
        self,
        path: str,
    ) -> None:
        conf: Config = await self.load_config(path)
        register_routes(
            self._app,
            conf,
            Data_Base(conf.db),
        )

    async def on_shutdown(
        self,
    ) -> None: ...


__all__: list[str] = [
    "Server",
]
