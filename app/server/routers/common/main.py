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
        router = APIRouter(prefix="/common")
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
                **common_routes[str(method.__name__)],
            )

        app.include_router(router)


__all__: list[str] = [
    "Common_Routers",
]
