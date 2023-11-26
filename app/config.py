#from pydantic import BaseSettings
import pydantic_settings

class Settings(pydantic_settings.BaseSettings):
    database_username: str
    database_password:str
    database_hostname: str
    database_name: str
    database_port: str
    secret_key : str
    algorithm : str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()