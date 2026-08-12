from langchain_community.document_loaders import TextLoader

from app.loaders.base import BaseDocumentLoader


class TxtLoader(BaseDocumentLoader):

    def load(self, file_path: str):

        loader = TextLoader(
            file_path=file_path,
            encoding="utf-8"
        )

        return loader.load()