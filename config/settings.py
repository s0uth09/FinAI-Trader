from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    database_url: str = "postgresql://user:password@localhost:5432/finai"
    redis_url: str = "redis://localhost:6379/0"
    secret_key: str = "your_secret_key"
    log_level: str = "INFO"
    binance_api_key: str
    # Add other keys...

settings = Settings()
