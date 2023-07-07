from .settings import *


class Common_Routers:
    class Routers:
        ...

    @classmethod
    def register_common_routers(
        cls,
        app: FastAPI,
        config: object,
        db: object,
    ) -> None:
        _apps: tuple[object] = cls.Routers.__bases__
        for _app in _apps:
            app.include_router(
                _app(
                    config,
                    db,
                ).router,
            )


__all__: list[str] = [
    "Common_Routers",
]
