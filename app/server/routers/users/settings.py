from fastapi import FastAPI, APIRouter

import inspect

users_routes: dict[str, dict] = {}


__all__: list[str] = [
    "FastAPI",
    "APIRouter",
    "inspect",
    "users_routes",
]
