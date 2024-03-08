from dataclasses import dataclass
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext


@dataclass
class DB_Config:
    dialect: str
    driver: str
    host: str
    password: str
    user: str
    database: str


@dataclass
class Crypt_Config:
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTS: str
    oauth2_scheme: OAuth2PasswordBearer
    pwd_context: CryptContext


@dataclass
class Config:
    db: DB_Config
    crypt: Crypt_Config


__all__: list[str] = [
    "DB_Config",
    "Crypt_Config",
    "Config",
]
