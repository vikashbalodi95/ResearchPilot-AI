from pypdf import PdfReader


class PDFService:

    def extract_text(self, file_path: str) -> str:
        reader = PdfReader(file_path)

        extracted_text = []

        for page in reader.pages:
            text = page.extract_text()

            if text:
                extracted_text.append(text)

        return "\n".join(extracted_text)