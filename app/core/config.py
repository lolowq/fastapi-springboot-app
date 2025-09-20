
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()  # Загружаем переменные из .env

class Settings(BaseSettings):
    # Настройки приложения
    APP_NAME: str = "FastAPI Spring Boot App"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # Настройки базы данных (аналог H2 in-memory)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    
    # Настройки сервера
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))
    
    class Config:
        env_file = ".env"

settings = Settings()
