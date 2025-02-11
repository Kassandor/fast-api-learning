# Project settings
import dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Настройки проекта
    """

    TEST_ENV_VAR: str

    model_config = SettingsConfigDict(env_file='base/.env', env_file_encoding='utf-8')


settings = Settings()
