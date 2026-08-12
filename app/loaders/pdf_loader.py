from langchain_community.document_loaders import PyPDFLoader

from app.loaders.base import BaseDocumentLoader


class PDFLoader(BaseDocumentLoader):

    def load(self, file_path: str):

        loader = PyPDFLoader(file_path)

        return loader.load()