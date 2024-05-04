from typing import Optional
from functools import lru_cache
from pydantic import PostgresDsn, field_validator, ValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    model_config = SettingsConfigDict(env_file="../../.env")

    @field_validator("SQLALCHEMY_DATABASE_URI", mode="after")
    def assemble_db_connection(cls, v: Optional[str], values: ValidationInfo) -> str:
        return PostgresDsn.build(
            scheme="postgresql",
            username=values.data.get("POSTGRES_USER"),
            password=values.data.get("POSTGRES_PASSWORD"),
            host=values.data.get("POSTGRES_SERVER"),
            port=int(values.data.get("POSTGRES_PORT")),
            path=f"{values.data.get('POSTGRES_DB') or ''}",
        )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
