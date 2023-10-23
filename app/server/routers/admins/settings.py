from fastapi import FastAPI, APIRouter

import inspect

admins_routes: dict[str, dict] = {}

__all__: list[str] = [
    "FastAPI",
    "APIRouter",
    "inspect",
    "admins_routes",
]
