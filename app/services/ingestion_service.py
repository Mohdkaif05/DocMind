from langchain_core.documents import Document

from app.loaders.loader_factory import LoaderFactory


class IngestionService:

    @staticmethod
    def load_document(
        file_path: str
    ) -> list[Document]:

        loader = LoaderFactory.get_loader(file_path)

        return loader.load(file_path)