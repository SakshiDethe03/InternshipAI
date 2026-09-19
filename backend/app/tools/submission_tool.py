from schemas.submitted_application import SubmittedApplication
from schemas.application_schema import ApplicationData


def submission_tool(application: ApplicationData) -> SubmittedApplication:
    """
    Mock tool that submits an approved internship application.
    """

    print("\n===================================")
    print("SUBMITTING APPLICATION")
    print("===================================")

    print("Application ID:", application.application_id)
    print("Internship ID:", application.internship_id)
    print("Candidate:", application.name)

    # Mock submission
    success = True

    if success:
        return SubmittedApplication(
            internship_id=application.internship_id,
            applicant_id=application.name,
            application_id=application.application_id,
            success=True,
            status="SUBMITTED",
            message="Application submitted successfully.",
        )

    return SubmittedApplication(
        internship_id=application.internship_id,
        applicant_id=application.name,
        application_id=application.application_id,
        success=False,
        status="FAILED",
        message="Application submission failed.",
    )
