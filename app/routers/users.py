from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.user import User
from app.services.user_service import UserService
from pydantic import BaseModel

# Request and Response models (analog of DTOs)
class UserCreate(BaseModel):
    email: str
    name: str

class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    
    class Config:
        from_attributes = True

# Create router (analog of @RestController)
router = APIRouter(prefix="/api/users", tags=["users"])

@router.get("/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    """Get all users (analog of @GetMapping)"""
    return UserService.get_all_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get user by ID (analog of @GetMapping("/{id}"))"""
    user = UserService.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    return user

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    """Create new user (analog of @PostMapping)"""
    try:
        return UserService.create_user(db, user_data.email, user_data.name)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Delete user by ID (analog of @DeleteMapping("/{id}"))"""
    if not UserService.delete_user(db, user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
