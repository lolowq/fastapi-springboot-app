from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Создаем engine (аналог DataSource в Spring)
engine = create_engine(
    settings.DATABASE_URL, 
    connect_args={"check_same_thread": False}  # Нужно только для SQLite
)

# Создаем SessionLocal (аналог EntityManager)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей (аналог @Entity)
Base = declarative_base()

# Dependency для получения сессии (аналог @PersistenceContext)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()