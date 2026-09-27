from app.tools.document_tool import DocumentTool


document_tool = DocumentTool()

pdf_path = r"E:\ResearchPilot AI\backend\data\research.pdf"

info = document_tool.get_document_info(pdf_path)

print("Filename:", info["filename"])
print("Characters:", info["characters"])
print("Words:", info["words"])
print("Extracted text:")
print(info["text"][:1000])