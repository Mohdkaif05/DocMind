from fastapi import FastAPI
from app.config import settings
from app.api.health import router as health_router
from app.api.upload import router as upload_router


app = FastAPI(

    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    debug=settings.DEBUG
)

app.include_router(health_router)


app.include_router(upload_router)

@app.get("/")
async def root():

    return {

        "message": "Welcome to AI Research Assistant"

    }