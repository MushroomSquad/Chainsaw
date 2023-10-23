from fastapi import FastAPI, APIRouter

import inspect

moders_routes: dict[str, dict] = {}

__all__: list[str] = [
    "FastAPI",
    "APIRouter",
    "inspect",
    "moders_routes",
]
