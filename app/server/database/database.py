from .methods import *
import inspect


class Data_Base:
    def __init__(
        self,
        host: str | None = None,
        password: str | None = None,
        user: str | None = None,
        database: str | None = None,
    ) -> None:
        self.queries = sql_queries
        _args, _local = inspect.signature(self.__init__), locals()
        self.connect_args: list[str] = [
            _local[param.name]
            for param in _args.parameters.values()
            if _local[param.name]
        ]

    async def create_connect(
        self,
        host: str | None = None,
        password: str | None = None,
        user: str | None = None,
        database: str | None = None,
    ):
        ...


__all__: list[str] = [
    "Data_Base",
]
