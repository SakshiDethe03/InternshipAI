from pydantic import BaseModel


class SubmittedApplication(BaseModel):
    internship_id: str
    applicant_id: str
    application_id: str
    success: bool
    status: str
    message: str
