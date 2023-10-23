from .settings import *


class Server:
    __app: FastAPI

    def __init__(
        self,
        app: FastAPI,
    ) -> None:
        self.__app = app

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

    async def on_startup(
        self,
        path: str,
    ) -> None:
        conf = await self.load_config(path)
        register_routes(
            self.__app,
            conf,
            Data_Base(conf.db),
        )

    async def on_shutdown(
        self,
    ) -> None:
        ...


__all__: list[str] = [
    "Server",
]
