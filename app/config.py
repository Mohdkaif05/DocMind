from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    PROJECT_NAME: str
    API_VERSION: str
    DEBUG: bool
    HOST: str
    PORT: int
    CHUNK_SIZE: int
    CHUNK_OVERLAP: int



    class Config:
        env_file = ".env"

settings = Settings()
