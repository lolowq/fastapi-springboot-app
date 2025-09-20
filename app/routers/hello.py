from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
async def hello_world():
    """Simple Hello World endpoint (Spring Boot analogue)"""
    return {
        "message": "Hello World from FastAPI Spring Boot analogue!", 
        "status": "success",
        "framework": "FastAPI (Python Spring Boot analogue)"
    }
