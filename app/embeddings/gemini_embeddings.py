from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.config import settings


class GeminiEmbeddingService:

    def __init__(
        self,
        model: str = "gemini-embedding-001"
    ):
        if not settings.GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY is not configured."
            )

        self.embeddings = GoogleGenerativeAIEmbeddings(
            model=model,
            google_api_key=settings.GEMINI_API_KEY
        )

    def embed_documents(
        self,
        texts: list[str]
    ) -> list[list[float]]:

        if not texts:
            return []

        return self.embeddings.embed_documents(texts)

    def embed_query(
        self,
        text: str
    ) -> list[float]:

        return self.embeddings.embed_query(text)