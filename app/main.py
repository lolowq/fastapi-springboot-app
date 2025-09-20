from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import engine, Base, get_db
from app.routers import users  # Import the router
from app.models.user import User

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers (analog of @ComponentScan)
app.include_router(users.router)

# Setup Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def root(request: Request, db: Session = Depends(get_db)):
    users = db.query(User).all()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "app_name": settings.APP_NAME,
            "users": users
        }
    )

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )

from app.routers import hello  # Add this import

# Добавляем после других app.include_router
app.include_router(hello.router)