from typing import TypedDict

from schemas.resume import Resume
from schemas.internship import Internship
from schemas.eligibility import EligibilityResult
from schemas.JD_matching import JDMatchingResult
from schemas.match_decision import MatchDecisionResult

from schemas.application_schema import ApplicationData

from schemas.submitted_application import SubmittedApplication

# from schemas.application_response import ApplicationResponse


class AIApplicationAgentState(TypedDict, total=False):

    # Candidate information
    resume: Resume

    # Internship Information
    internships: list[Internship]
    selected_internship: Internship

    # Application Results
    eligibility_results: dict[str, EligibilityResult]
    jd_matching_results: dict[str, JDMatchingResult]
    match_decisions: dict[str, MatchDecisionResult]

    # Application
    application_data: dict[str, ApplicationData]

    # User approval
    approval_status: dict[str, str]

    # Final submission
    submitted_applications: dict[str, SubmittedApplication]
