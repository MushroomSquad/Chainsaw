from fastapi import FastAPI
from .routers import register_routes
from dataclasses import dataclass
from environs import Env
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from .database import Data_Base


@dataclass
class DB_Config:
    host: str
    password: str
    user: str
    database: str


@dataclass
class Crypt_Config:
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTS: str
    oauth2_scheme: object
    pwd_context: object


@dataclass
class Config:
    db: DB_Config
    crypt: Crypt_Config
