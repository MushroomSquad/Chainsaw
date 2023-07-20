from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from .methods import *


class Data_Base:
    def __init__(
        self,
        conf,
    ) -> None:
        self.queries = sql_queries
        if conf.user and conf.password:
            self.url: str = f"{conf.dialect}+{conf.driver}://{conf.user}:{conf.password}@{conf.host}/{conf.database}"
        else:
            self.url: str = f"{conf.dialect}+{conf.driver}:///{conf.host}"
        self.init_session()

    def init_session(
        self,
    ):
        self.session = async_sessionmaker(
            create_async_engine(
                self.url,
                echo=True,
            ),
            expire_on_commit=False,
        )


__all__: list[str] = [
    "Data_Base",
]
