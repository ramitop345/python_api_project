from pydantic_settings import BaseSettings
from dotenv import load_dotenv

class Settings(BaseSettings):
    database_hostname: str
    database_password: str
    database_username: str
    database_port: str
    database_name: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    
load_dotenv()

settings = Settings()