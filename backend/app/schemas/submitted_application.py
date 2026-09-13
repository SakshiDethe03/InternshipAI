from pydantic import BaseModel
from typing import List


class SubmittedApplication(BaseModel):
    internship_id: str
    applicant_id: str
    application_id: str
    success: bool
    status: str
    message: str
