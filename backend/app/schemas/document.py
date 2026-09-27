from pydantic import BaseModel, Field


class UploadDocumentRequest(BaseModel):
    filename: str = Field(..., min_length=1)
    file_size_bytes: int = Field(..., ge=1)
    content_type: str = Field(default="application/pdf")
