import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os

class OCRService:
    def extract_text(self, file_path: str, mime_type: str) -> str:
        if mime_type == "application/pdf":
            return self._extract_from_pdf(file_path)
        else:
            return self._extract_from_image(file_path)

    def _extract_from_pdf(self, path: str) -> str:
        pages = convert_from_path(path)
        return "\n".join(pytesseract.image_to_string(p) for p in pages)

    def _extract_from_image(self, path: str) -> str:
        image = Image.open(path)
        return pytesseract.image_to_string(image)
