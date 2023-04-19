import os
import pathlib

from pydantic import BaseSettings

WORK_PATH = pathlib.Path(__name__).resolve().parent
AVATAR_PATH = WORK_PATH / "FileResource"
setting_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "settings")


class Settings(BaseSettings):
    APP_NAME: str
    SQLALCHEMY_DATABASE_URI: str
    FIRST_SUPERUSER: str
    FIRST_SUPERUSER_PASSWORD: str
    SECRET_KEY: str
    ENVIRONMENT: str = "DEV"


class Production(Settings):
    class Config:
        # 生产环境配置单独上传,不提交至git
        env_file = os.path.join(setting_file_path, ".env")
        env_file_encoding = 'utf-8'


class Testing(Settings):
    class Config:
        env_file = os.path.join(setting_file_path, ".testing.env")
        env_file_encoding = 'utf-8'


class Dev(Settings):
    class Config:
        env_file = os.path.join(setting_file_path, ".dev.env")
        env_file_encoding = 'utf-8'


def get_settings():
    env = os.getenv("INTOUSERENV", "DEV")
    print(env)
    _inst = Dev()
    if env == "TESTING":
        _inst = Testing()
    if env == "PRODUCTION":
        _inst = Production()
    _inst.ENVIRONMENT = env
    return _inst


settings = get_settings()
# settings.CHAIN = {}
# settings.API = {}
