from langchain_core.documents import Document

from app.embeddings.gemini_embeddings import (
    GeminiEmbeddingService
)


class EmbeddingService:

    def __init__(self):
        self.embedding_model = GeminiEmbeddingService()

    def embed_chunks(
        self,
        chunks: list[Document]
    ) -> list[list[float]]:

        if not chunks:
            return []

        texts = [
            chunk.page_content
            for chunk in chunks
        ]

        return self.embedding_model.embed_documents(
            texts
        )

    def embed_query(
        self,
        query: str
    ) -> list[float]:

        return self.embedding_model.embed_query(
            query
        )

## We don't want upload.py directly talking to Gemini- Provide layer of abstraction