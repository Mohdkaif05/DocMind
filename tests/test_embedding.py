from app.embeddings.gemini_embeddings import GeminiEmbeddingService



embedding_service = GeminiEmbeddingService()

vector = embedding_service.embed_query(
    "Transformers use self-attention."
)

print("Embedding dimensions:", len(vector))
print("First 10 values:", vector[:10])