from abc import ABC, abstractmethod

from langchain_core.documents import Document


class BaseDocumentLoader(ABC):

    @abstractmethod
    def load(
        self,
        file_path: str
    ) -> list[Document]:
        """
        Load a document and return LangChain Documents.
        """
        pass