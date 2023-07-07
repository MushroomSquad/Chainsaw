from typing import Callable
from fastapi import FastAPI
from .admins import Admins_Routers
from .moders import Moders_Routers
from .users import Users_Routers
from .common import Common_Routers


def register_routes(
    app: FastAPI,
    config: object,
    db: object,
) -> None:
    routers: tuple[Callable[[FastAPI, object, object], None], ...] = (
        Admins_Routers.register_admins_routers,
        Moders_Routers.register_moders_routers,
        Users_Routers.register_users_routers,
        Common_Routers.register_common_routers,
    )
    for router in routers:
        router(
            app,
            config,
            db,
        )


__all__: list[str] = [
    "register_routes",
]
