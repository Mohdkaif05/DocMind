from pathlib import Path
import shutil

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.ingestion_service import IngestionService
from app.chunking.recursive_chunker import TextChunker


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
        # 1. Save uploaded file
        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        file_size = destination.stat().st_size

        # 2. Load document
        documents = IngestionService.load_document(
            str(destination)
        )

        # 3. Split document into chunks
        chunker = TextChunker()

        chunks = chunker.split_documents(
            documents
        )

        # 4. Get chunk statistics
        chunk_statistics = chunker.get_statistics(
            chunks
        )

        # 5. Create preview of first 3 chunks
        chunk_preview = [
            {
                "chunk_index": chunk.metadata.get(
                    "chunk_index"
                ),
                "chunk_size": chunk.metadata.get(
                    "chunk_size"
                ),
                "metadata": chunk.metadata,
                "content_preview": chunk.page_content[:300]
            }
            for chunk in chunks[:3]
        ]

        return {
            "status": "success",
            "filename": file.filename,
            "size_bytes": file_size,
            "documents_loaded": len(documents),
            "chunks_created": len(chunks),
            "chunk_statistics": chunk_statistics,
            "chunk_preview": chunk_preview
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