from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import settings


class TextChunker:

    def __init__(
        self,
        chunk_size: int = settings.CHUNK_SIZE,
        chunk_overlap: int = settings.CHUNK_OVERLAP
    ):
        if chunk_size <= 0:
            raise ValueError(
                "chunk_size must be greater than 0"
            )

        if chunk_overlap < 0:
            raise ValueError(
                "chunk_overlap cannot be negative"
            )

        if chunk_overlap >= chunk_size:
            raise ValueError(
                "chunk_overlap must be smaller than chunk_size"
            )

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def split_documents(
        self,
        documents: list[Document]
    ) -> list[Document]:

        chunks = self.splitter.split_documents(documents)

        for index, chunk in enumerate(chunks):
            chunk.metadata["chunk_index"] = index
            chunk.metadata["chunk_size"] = len(
                chunk.page_content
            )

        return chunks

    @staticmethod
    def get_statistics(
        chunks: list[Document]
    ) -> dict:

        if not chunks:
            return {
                "total_chunks": 0,
                "average_chunk_size": 0,
                "min_chunk_size": 0,
                "max_chunk_size": 0
            }

        sizes = [
            len(chunk.page_content)
            for chunk in chunks
        ]

        return {
            "total_chunks": len(chunks),
            "average_chunk_size": round(
                sum(sizes) / len(sizes),
                2
            ),
            "min_chunk_size": min(sizes),
            "max_chunk_size": max(sizes)
        }