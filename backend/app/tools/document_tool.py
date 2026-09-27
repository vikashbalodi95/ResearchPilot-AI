from app.services.pdf_service import PDFService


class DocumentTool:

    def __init__(self):
        self.pdf_service = PDFService()

    def get_document_info(self, file_path: str):

        text = self.pdf_service.extract_text(file_path)

        return {
            "filename": file_path,
            "characters": len(text),
            "words": len(text.split()),
            "text": text,
        }