from langchain_community.document_loaders import Docx2txtLoader

from app.loaders.base import BaseDocumentLoader


class DocxLoader(BaseDocumentLoader):

    def load(self, file_path: str):

        loader = Docx2txtLoader(file_path)

        return loader.load()