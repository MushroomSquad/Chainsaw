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
        env: Env = Env()
        env.read_env(path)
        return Config(
            db=DB_Config(
                dialect=env.str("DIALECT"),
                driver=env.str("DB_DRIVER"),
                host=env.str("DB_HOST"),
                password=env.str("DB_PASS"),
                user=env.str("DB_USER"),
                database=env.str("DB_NAME"),
            ),
            crypt=Crypt_Config(
                SECRET_KEY=env.str("SECRET_KEY"),
                ALGORITHM=env.str("ALGORITHM"),
                ACCESS_TOKEN_EXPIRE_MINUTS=env.int("ACCESS_TOKEN_EXPIRE_MINUTS"),
                oauth2_scheme=OAuth2PasswordBearer(tokenUrl=env.str("tokenUrl")),
                pwd_context=CryptContext(
                    schemes=env.list("schemes"),
                    deprecated=env.str("deprecated"),
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
