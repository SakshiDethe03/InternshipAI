from pydantic import BaseModel
from typing import List, Optional


class ApplicationData(BaseModel):
    internship_id: str

    # Applicant info
    name: str
    email: str
    phone: str
    linkedin: str
    github: Optional[str] = None

    # Applicant Resume
    resume: str

    # Application Cover Letter
    cover_letter: str

    # Application answers
    answers: dict[str, str]
