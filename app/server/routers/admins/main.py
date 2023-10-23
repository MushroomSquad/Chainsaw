from .settings import *


class Admins_Routers:
    class Routers:
        ...

    @classmethod
    def register_admins_routers(
        cls,
        app: FastAPI,
        config: object,
        db: object,
    ) -> None:
        router = APIRouter(prefix="/admin")
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
                **admins_routes[str(method.__name__)],
            )

        app.include_router(router)


__all__: list[str] = [
    "Admins_Routers",
]
