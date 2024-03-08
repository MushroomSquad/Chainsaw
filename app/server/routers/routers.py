from typing import TYPE_CHECKING, Callable
from fastapi import FastAPI


if TYPE_CHECKING:
    from ..models import Config
    from ..database import Data_Base


def register_routes(
    app: FastAPI,
    config: "Config",
    db: "Data_Base",
) -> None:
    routers: tuple[
        Callable[
            [
                FastAPI,
                "Config",
                "Data_Base",
            ],
            None,
        ],
        ...,
    ] = ()
    for router in routers:
        router(
            app,
            config,
            db,
        )


__all__: list[str] = [
    "register_routes",
]
