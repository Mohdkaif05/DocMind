from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health():

    return {
        "status": "healthy",
        "message": "DocMind API is running"
    }

