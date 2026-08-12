from pathlib import Path

from app.loaders.pdf_loader import PDFLoader
from app.loaders.docx_loader import DocxLoader
from app.loaders.txt_loader import TxtLoader


class LoaderFactory:

    LOADERS = {
        ".pdf": PDFLoader,
        ".docx": DocxLoader,
        ".txt": TxtLoader,
    }

    @classmethod
    def get_loader(
        cls,
        file_path: str
    ):

        extension = Path(file_path).suffix.lower()

        loader = cls.LOADERS.get(extension)

        if loader is None:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        return loader()