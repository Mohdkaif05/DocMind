from fastapi import FastAPI
from app.config import settings
from app.api.health import router as health_router


app = FastAPI(

    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    debug=settings.DEBUG
)

app.include_router(health_router)

@app.get("/")
async def root():

    return {

        "message": "Welcome to AI Research Assistant"

    }