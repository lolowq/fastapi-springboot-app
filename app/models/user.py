﻿from sqlalchemy import Column, Integer, String
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    
    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, name={self.name})>"
