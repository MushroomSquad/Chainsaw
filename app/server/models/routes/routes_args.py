from collections.abc import Callable, Sequence
from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any, Type

from fastapi.datastructures import DefaultPlaceholder
from fastapi import Response, params
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from fastapi.types import IncEx
from fastapi.utils import generate_unique_id
from starlette.routing import BaseRoute


@dataclass
class Route_Args:
    path: str
    response_model: Any = None
    status_code: int | None = None
    tags: list[str | Enum] | None = None
    dependencies: Sequence[params.Depends] | None = None
    summary: str | None = None
    description: str | None = None
    response_description: str = "Successful Response"
    responses: dict[int | str, dict[str, Any]] | None = None
    deprecated: bool | None = None
    methods: set[str] | list[str] | None = None
    operation_id: str | None = None
    response_model_include: IncEx | None = None
    response_model_exclude: IncEx | None = None
    response_model_by_alias: bool = True
    response_model_exclude_unset: bool = False
    response_model_exclude_defaults: bool = False
    response_model_exclude_none: bool = False
    include_in_schema: bool = True
    response_class: Type[Response] | DefaultPlaceholder = JSONResponse
    name: str | None = None
    route_class_override: Type[APIRoute] | None = None
    callbacks: list[BaseRoute] | None = None
    openapi_extra: dict[str, Any] | None = None
    generate_unique_id_function: Callable[[APIRoute], str] | DefaultPlaceholder = (
        generate_unique_id
    )

    def dict(
        self,
    ) -> dict:
        return {k: v for k, v in asdict(self).items()}


__all__: list[str] = [
    "Route_Args",
]
