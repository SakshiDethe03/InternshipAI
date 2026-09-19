from pydantic import BaseModel
from typing import Optional


class ApplicationData(BaseModel):
    application_id: str
    internship_id: str

    status: str

    # Applicant info
    name: str
    email: str
    phone: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None

    # Applicant Resume
    resume: str

    # Application Cover Letter
    cover_letter: str

    # Application answers
    answers: dict[str, str]
