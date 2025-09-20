from sqlalchemy.orm import Session
from app.models.user import User

class UserService:
    """Service class for user operations (analog of @Service in Spring)"""
    
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> User:
        """Get user by ID (analog of JpaRepository.findById)"""
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def get_all_users(db: Session) -> list[User]:
        """Get all users (analog of JpaRepository.findAll)"""
        return db.query(User).all()
    
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> User:
        """Get user by email"""
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def create_user(db: Session, email: str, name: str) -> User:
        """Create new user (analog of JpaRepository.save)"""
        # Check if user already exists
        existing_user = UserService.get_user_by_email(db, email)
        if existing_user:
            raise ValueError(f"User with email {email} already exists")
        
        # Create new user
        db_user = User(email=email, name=name)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def delete_user(db: Session, user_id: int) -> bool:
        """Delete user by ID"""
        user = UserService.get_user_by_id(db, user_id)
        if user:
            db.delete(user)
            db.commit()
            return True
        return False

# Analog of @Autowired through dependency injection