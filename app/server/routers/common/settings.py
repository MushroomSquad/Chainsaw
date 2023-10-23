from fastapi import FastAPI, APIRouter


import inspect

common_routes: dict[str, dict] = {}
__all__: list[str] = [
    "FastAPI",
    "APIRouter",
    "inspect",
    "common_routes",
]
