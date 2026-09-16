from pathlib import Path
from pypdf import PdfReader
from docx import Document


def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDf resume."""

    reader = PdfReader(file_path)

    text = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text.append(page_text.strip())

    return "\n".join(text).strip()


def extract_text_from_docx(file_path: str) -> str:
    """Extract text from DOCX resume."""

    document = Document(file_path)

    paragraphs = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            paragraphs.append(paragraph.text.strip())

    return "\n".join(paragraphs).strip()


def extract_resume_text(file_path: str) -> str:
    """
    Extract resume text based on the file extension.
    Supports PDF and DOCX files.
    """

    path = Path(file_path)

    extension = path.suffix.lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    elif extension == ".docx":
        return extract_text_from_docx(file_path)

    else:
        raise ValueError(
            f"Unsupported file type: {extension}. Please provide a PDF or DOCX file."
        )
