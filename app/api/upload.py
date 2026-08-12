from pathlib import Path
import shutil

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.ingestion_service import IngestionService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):
    if file.filename is None:
        raise HTTPException(
            status_code=400,
            detail="Filename is missing."
        )

    destination = UPLOAD_DIR / file.filename

    try:
        # Save uploaded file
        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Get file size
        file_size = destination.stat().st_size

        # Load document using LangChain
        documents = IngestionService.load_document(str(destination))

        return {
            "status": "success",
            "filename": file.filename,
            "size_bytes": file_size,
            "documents_loaded": len(documents),
            "metadata": documents[0].metadata if documents else {}
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process document: {str(e)}"
        )