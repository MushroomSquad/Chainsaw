from .settings import *


class Moders_Routers:
    class Routers:
        ...

    @classmethod
    def register_moders_routers(
        cls,
        app: FastAPI,
        config: object,
        db: object,
    ) -> None:
        router = APIRouter(prefix="/moder")
        attrs = (
            getattr(cls.Routers(), name)
            for name in dir(
                cls.Routers(),
            )
        )
        methods = list(filter(inspect.isfunction, attrs))
        for method in methods:
            router.add_api_route(
                endpoint=method,
                **moders_routes[str(method.__name__)],
            )

        app.include_router(router)


__all__: list[str] = [
    "Moders_Routers",
]
