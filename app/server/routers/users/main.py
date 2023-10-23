from .settings import *


class Users_Routers:
    class Routers:
        ...

    @classmethod
    def register_users_routers(
        cls,
        app: FastAPI,
        config: object,
        db: object,
    ) -> None:
        router = APIRouter(prefix="/user")
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
                **users_routes[str(method.__name__)],
            )

        app.include_router(router)


__all__: list[str] = [
    "Users_Routers",
]
